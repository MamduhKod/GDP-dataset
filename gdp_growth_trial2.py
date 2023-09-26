import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
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

#First clean growth
# Z score
def plot_years(year):
    data_growth[year].plot()

years_to_plot = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

for year in years_to_plot:
    plot_years(year)

# Plot the original years
for year in years_to_plot:
    data_growth[year].plot()
    
# clean them up and plot again

def clean_growth(year):
    column_name = year
    z_scores = np.abs((data_growth[column_name] - data_growth[column_name].mean()) / data_growth[column_name].std())
    z_threshold = 3
    df_cleaned = data_growth[z_scores < z_threshold]
    df_cleaned[year].plot()
    data_growth.drop(data_growth[z_scores >= z_threshold].index, inplace=True)

years_to_clean = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

for year in years_to_clean:
    clean_growth(year)

# Plot the cleaned data for each year
for year in years_to_clean:
    data_growth[year].plot()
    
    
# Then clean prevalence

# Create a new dataframe with the averages for each year

