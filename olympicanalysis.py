# -*- coding: utf-8 -*-
"""DS Ques 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SSEK7-cmK_VYfHmTWB8UxU75K__61IYs
"""

import pandas as pd
import numpy as np

df = pd.read_csv('/content/Olympics.csv')

# A

# Retrieve all records from the Olympics table

df

# B

# Retrieve only the Athlete names and the Medals they won

athlete_and_medal = print(df[['name', 'medal']])

# C

# Count the total number of athletes in the dataset.

total_athletes = print(df['name'].nunique())

# D

# Find all records of athletes who won a Gold medal

gold_medals_df = print(df[df['medal'] == 'Gold'])

# E

# List all athletes who won Silver, ordered by the Year they won it.

silver_medals_df = df[df['medal'] == 'Silver'].sort_values(by='year')
print(silver_medals_df[['name', 'year']])

# F

# Count how many Gold, Silver, and Bronze medals each country has won.

medals_by_country = print(df.groupby('noc')['medal'].value_counts().unstack(fill_value=0))

# G

# Identify countries that have won more than 50 Gold medals.

gold_medal = df[df['medal'] == 'Gold']
gold_medal_counts = print(gold_medal.groupby('noc').size())

# I

# Find the athlete who has won the most medals.

athlete_most_medals = print(df['name'].value_counts().idxmax())

# J

# List all events that include the term 'Freestyle' in their name.

freestyle_events = print(df[df['event'].str.contains('Freestyle', case=False)]['event'].unique())

# K

# Find the top 3 athletes by the total number of medals won in each sport.

athlete_medal_counts = df.groupby(['sport', 'name'])['medal'].count().reset_index()
athlete_rankings = athlete_medal_counts.sort_values(by=['medal'], ascending=False).head(3)
athlete_rankings

# L

# List athletes who won more than one medal in a single Olympic year.

athlete_medal_counts = df.groupby(['year', 'name'])['medal'].count().reset_index()
multi_medal_winners = athlete_medal_counts[athlete_medal_counts['medal'] > 1].sort_values(by='medal',ascending=False)
multi_medal_winners

# M

# Identify countries that have won gold medals in both Summer and Winter Olympics.

gold_medals_season = df[df['medal'] == 'Gold'].groupby(['noc', 'season']).size().unstack(fill_value=0)
countries_both_seasons = gold_medals_season[(gold_medals_season['Summer'] > 0) & (gold_medals_season['Winter'] > 0)].index.tolist()
print(countries_both_seasons)

# N

# Show the year difference between the first and last medal won by each country.

first_last_medal_years = df.groupby('noc')['year'].agg(['min', 'max'])
first_last_medal_years['Year_Difference'] = first_last_medal_years['max'] - first_last_medal_years['min']
print(first_last_medal_years[['Year_Difference']])

# S

# List countries that have won medals in more than 10 different sports.

countries_multiple_sports = df.groupby('noc')['sport'].nunique()
countries_more_than_10_sports = countries_multiple_sports[countries_multiple_sports > 10].index.tolist()
print(countries_more_than_10_sports)