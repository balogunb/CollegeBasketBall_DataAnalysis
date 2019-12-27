# CollegeBasketBall_DataAnalysis

Programming Language: Python

Author: Basit Balogun


INTRODUCTION
This repository contains analysis on College Basketball dataset to make inferences and predictions. The dataset contains a total of 355 teams accross 33 Division 1 conferences. It contains data from 2015 - 2019. The data is gotten from kaggle and the link would be listed below. I used the cbb.csv file for all analysis and the file analysis.py is the main script to be run.

Link: https://www.kaggle.com/andrewsundberg/college-basketball-dataset/data




REQUIRED DEPENDECIES 
- pandas 
- matplotlib.pyplot



RESULTS 
- Cleaned data by replacing all null values with 0
- Determined the total number of teams in the data set 
  Total number of teams = 355
- Determined the number of D1 conferences covered 
  Total number of D1 conferences covered = 33
- Random check to see if it contained information on my school, Lafayette college which it did 
- Split dataset into different datasets by year and exported them to new csv files
  The csv files are contained in this repo. They all start with 'CollegeBB_stats'
- Determined the most competitive conferences using data on teams' power rating. Achieved this by converting the list containing college data to a list of the average power rating for each conferences 
- Focusing on the top 10 conferences by power ranking, monitored the change in ranking over the years the data set covers. A visual representation of this data can be found in the png file 'Top10ConferencesbyPowerRanking_2019'


Further Analysis Coming soon



