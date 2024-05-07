# NBA-Model
This project seeks to predict nba players's statistical outputs in the categories of points, rebounds, and assists, by using a forcasting regression model. 

The data comes in the form of a JSON from an api call, where a specific player is specified, and all of that player's games played so far during this NBA season are returned, as well as relevant statistics and information such as points scored, shots taken, field goal %, and opponent played amongst many others. 

Some preprocessing was done, by altering the JSON file to be put into a dataframe, and creating new columns in the dataframe to hold lagged values for points, assists, and rebounds in order to perform a time series analysis. Additionally rows containing missing values were dropped. 

The model selected was a random forest regressor, and a number of different lag window sizes were experimented with, ranging from 1 to 15, with the best windows seemingly being 7 or 9, although this also seems to change based on different players and their performances. 

Results and notes: 

Initially, prior to adding a time series analysis the mean squared error was hanging roughly around 10. After adding a time series analysis and experimenting with different lag window sizes, at best I was able to reduce mean squared error by a little over 40%, getting it down to about 5.9. Some unusual issues were that some players prompted a very small error, down to less than 1. This seems unrealistic, and was likely an issue with the data itself, although I havent identified that issue yet. 
