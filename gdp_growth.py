import pandas as pd
import matplotlib.pyplot as plt

# The goal of the project is to visualize if the growth of GDP corresponds
# to a decrease in mental health issues

# First looking at the world economy as a whole

data1 = pd.read_csv('gdp_growth.csv')
data1
data1 = data1.set_index('Country Name')
data1 = data1.T
data1 = data1.iloc[31:]
data1.iloc[0]
data1

#Data on mental health
data2 = pd.read_csv('/Users/mamduhhalawa/Desktop/GDP dataset/share-with-depression.csv')

data2 = data2.set_index("Year")
data2
data2.rename(columns={'Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)':'Prevalence'}, inplace=True)


#take 1990 as example

prev_1990 = data2[data2["Year"] == 1990]
prev_1990.rename(columns={'Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)':'Prevalence'}, inplace=True)
prev_1990.set_index('Entity')

prev_1990.merge(data1)


summed_prev = []

for entity in data2['Entity']:
        if entity in summed_prev:
            continue
        summed_prev.append(entity)
        

summed_prev

for country in summed_prev:
    data2['Prevalence'].sum()

    
    


#Same analysis based on countr average