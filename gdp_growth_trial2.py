import pandas as pd
import matplotlib.pyplot as plt

# Visualize how economic growth correlates with 
# the prevalence of depression last 10 years

data_growth = pd.read_csv('gdp_growth.csv')
data_growth = data_growth.drop(data_growth.iloc[:,1:53], axis=1)
data_growth

data_prev = pd.read_csv('/Users/mamduhhalawa/Desktop/GDP dataset/share-with-depression.csv')
data_prev.rename(columns={"Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)": "Prevalence"}, inplace=True)
data_prev

data_prev = data_prev[data_prev['Year'] > 2010]
data_prev

#remove the extreme values for each year

#First growth
q1_2012 = data_growth['2012'].quantile(0.25)
q3_2012 = data_growth['2012'].quantile(0.75)
IQR_2012 = q3_2012 - q1_2012

lower_bound_2012 = q1_2012 - 1.5 * IQR_2012
upper_bound_2012 = q3_2012 + 1.5 * IQR_2012

filtered_growth_2012 = data_growth[(data_growth>= lower_bound_2012) &(data_growth<= upper_bound_2012)]

#Summarize the total rates for each year


#plot the interaction