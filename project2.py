#Aim of this project for the Olympics data is to analyze with the following details:
#The data has the first four rows with non tabular form, so read it by skipping these rows initially while loading it
import pandas as pd
import numpy as np
olympic = pd.read_csv('C:/Users/ROY/Desktop/ULTIMATE DATA SCIENCE IN UDEMY/Pandas_Project_Session//data/olympics/olympics1.csv',skiprows=4)
print(olympic)
print('the total_number of rows is:',olympic.shape[0],print('the total_number of columns is:',olympic.shape[1],
print('the total number of rows and columns is:',olympic.shape)))
print(olympic.info())
print(olympic.describe())

#Find In which events did Edwin Flack win a medal?
EF=olympic[(olympic['Athlete']=='FLACK, Edwin')]
print(EF['Event'].value_counts())

#Which country has won the most men's gold medals in Athletics over the years? Sort the results alphabetically by the player's names
gold_medal=olympic[(olympic.Sport=='Athletics')&(olympic.Gender=='Men')&(olympic.Medal=='Gold')]
print(gold_medal)
mens=gold_medal.sort_values(by='Athlete')
print(mens)
print(mens['NOC'].value_counts())
print(len(mens['NOC'].value_counts()))

#How many gold medals the Indian Men's have won and name the event also?
indian_medals=olympic[(olympic['NOC']=='IND')&(olympic['Gender']=='Men')&(olympic['Medal']=='Gold')]
print(indian_medals['Event'].value_counts())
print(len(indian_medals['Event'].value_counts()))

#Check to see how many Indian women's have won the gold, silver or branze medals in the Olympic games?
W_gold=olympic[(olympic['NOC']=='IND')&(olympic['Gender']=='Women')&(olympic['Medal']=='Gold')]
print(W_gold)
W_silver=olympic[(olympic['NOC']=='IND')&(olympic['Gender']=='Women')&(olympic['Medal']=='Silver')]
print(W_silver)
W_bronze=olympic[(olympic['NOC']=='IND')&(olympic['Gender']=='Women')&(olympic['Medal']=='Bronze')]
print(W_bronze)

#Which five countries have won the most medals in recent years (from 2000 to 2008)?
rec_medal=olympic[(olympic['Edition']>=2000)]
recent_medal=rec_medal.sort_values(by='Medal',ascending=False)
print(recent_medal.head(n=5))
print(recent_medal['NOC'].value_counts().head(n=5))

#Display the male gold medal winners for the hockey event over the years. List the results starting with 
# the most recent. Show the Olympic City, Edition, Athlete and the country they represent.
hockey_men=olympic[(olympic['Gender']=='Men')&(olympic['Sport']=='Hockey')&(olympic['Medal']=='Gold')]
male_winner=hockey_men.sort_values(by='Edition',ascending=False)
dropped_columns=male_winner.drop(columns=['Sport','Discipline','Gender','Event','Event_gender','Medal'])
print(dropped_columns)
top_winner=dropped_columns.head(n=1)
print(top_winner['Athlete'].value_counts())

#How many women have won the gold medal's till 2008 in Olympic game
gold_women=olympic[(olympic['Gender']=='Women')&(olympic['Medal']=='Gold')]
sgold_women=gold_women.sort_values(by='Athlete',ascending=True).drop_duplicates()
print(sgold_women['Athlete'].value_counts())


