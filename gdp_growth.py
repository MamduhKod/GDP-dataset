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
data1.loc['1990']
data1



#Data on mental health
data2 = pd.read_csv('/Users/mamduhhalawa/Desktop/GDP dataset/share-with-depression.csv')

data2 = data2.set_index("Year")
data2
data2.rename(columns={'Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)':'Prevalence'}, inplace=True)
data2


#Visualize relationship between country growth rates in 1990, and their prevalence of mental health issues

prev_1990 = data2[data2["Year"] == 1990]
prev_1990.set_index('Entity')

prev_1990_sorted=prev_1990.sort_values(by='Prevalence',ascending=False)

prev_1990_sorted.plot(y='Prevalence', kind='bar')
prev_1990

growth_1990 = data1.loc['1990']
growth_frame = pd.DataFrame(growth_1990)
sorted_growth = growth_frame['1990'].sort_values(ascending=False)

# Investigate the 30 highest growing economies and their prevalence of mental health issues
top_growth = sorted_growth.iloc[:30]
top_growth = pd.DataFrame(top_growth)
top_growth

top_prev = prev_1990_sorted.iloc[:30]
top_prev.merge(top_growth)
top_growth.rename(columns={'1990':'Growth rate 1990'}, inplace=True)
top_growth

result = pd.concat([top_growth, top_prev], axis=1)
result.info()

result = result['Year'].convert_dtypes(str)
result.info()
result 








    
    


#Same analysis based on countr average