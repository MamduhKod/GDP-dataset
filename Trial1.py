# Putting the old approach here - I messed it up but want to save it

import pandas as pd
import matplotlib.pyplot as plt

# The goal of the project is to visualize if the growth of GDP corresponds
# to a decrease in mental health issues

# First looking at the world economy as a whole
#Visualize relationship between country growth rates in 1990, and their prevalence of mental health issues


data1 = pd.read_csv('gdp_growth.csv')
data1
data1.drop(data1.iloc[:, 2:33], inplace=True, axis=1)
data1

data1.drop(data1.iloc[:, 3:33], inplace=True, axis=1)
data1



#Data on mental health
data2 = pd.read_csv('/Users/mamduhhalawa/Desktop/GDP dataset/share-with-depression.csv')
data2
data2.rename(columns={'Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)':'Prevalence'}, inplace=True)
data2

#Visualize relationship between country growth rates in 1990, and their prevalence of mental health issues






prev_1990 = data2[data2["Year"] == 1990]
prev_1990

sorted_prev=prev_1990.sort_values(by='Prevalence',ascending=False)
sorted_prev

sorted_growth = data1.sort_values(by='1991',ascending=False)
sorted_growth = sorted_growth.rename(columns={'Country Name': 'Entity2'})
sorted_growth
result = pd.concat([sorted_growth, sorted_prev], axis=1)
result

combined_column = pd.concat([result['Entity2'], result['Entity']])
combined_column

Unique_countries = combined_column.drop_duplicates().reset_index(drop=True)
Unique_countries

result['Unique Countries'] = Unique_countries
result

result['Unique Countries'].info()


result['merged'] = pd.concat([sorted_growth['Country Name'], sorted_prev['Entity']])









    
    


#Same analysis based on countr average