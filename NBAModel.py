import json
import config
import numpy as np
import pandas as pd
from pandas import concat
from requests.auth import HTTPBasicAuth
import requests
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

#API URL and Key
api_url = 'https://api.balldontlie.io/v1/stats'
api_key = config.api_key

#Defining Headers and parameters
headers = {
    'Authorization' : api_key
}
payload= {'seasons[]' : '2023', 'player_ids[]' : '22', 'start_date':'2023-10-24', 'end_date':'2024-04-04', 'per_page':'100'}

#Querying the API
response =requests.get(api_url, headers=headers, params = payload)

#Parsing JSON response for points, rebounds, and assists and storing them in lists
if response.status_code == 200:
    data = response.json()
    data_list = data['data']
    df = pd.json_normalize(data_list)
#Handling API access error
else:
    print(response.status_code)

#function for creating lagged data

lags = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for lag in lags:
    df[f'lagged_pts_{lag}'] = df['pts'].shift(lag)
    df[f'lagged_ast_{lag}'] = df['ast'].shift(lag)
    df[f'lagged_reb_{lag}'] = df['reb'].shift(lag)

results = []

for lag in lags:
    # Select lagged features
    X = df[[f'lagged_pts_{lag}', f'lagged_ast_{lag}', f'lagged_reb_{lag}']]
    y = df[['pts', 'reb', 'ast']]
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    
    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    
    # Make predictions
    prediction = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = np.sqrt(mean_squared_error(y_test, prediction))
    
    results.append({'lag': lag, 'accuracy': accuracy})

# Print results
for result in results:
    print(f"Lag: {result['lag']}, Accuracy: {result['accuracy']}")




























































