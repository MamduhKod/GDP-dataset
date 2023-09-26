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

#Plot original data
def plot_prev_origin(year):
 data_prev[data_prev['Year'] ==year]['Prevalence'].plot()
 
prev_years_to_plot = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
for year in prev_years_to_plot:
 plot_prev_origin(year)

data_prev.describe()
# clean it up and plot again

def remove_outliers_and_plot(data_frame, year_range):
    for year in year_range:
        # Filter the DataFrame for the specified year
        data_year = data_frame[data_frame['Year'] == year]

        # Calculate z-scores for the 'Prevalence' column
        z_scores = np.abs((data_year['Prevalence'] - data_year['Prevalence'].mean()) / data_year['Prevalence'].std())

        # Set the z-score threshold for outlier removal
        z_threshold = 3

        # Remove outliers and assign the cleaned data back to the DataFrame
        data_year_cleaned = data_year[z_scores < z_threshold]

        data_frame[data_frame['Year'] == year] = data_year_cleaned

# Define the range of years you want to process
year_range = range(2013, 2020)

# Call the function to remove outliers and plot for the specified years
remove_outliers_and_plot(data_prev, year_range)


# Create a new dataframe with the averages for each year

new_list = []

data_prev[data_prev['Year'] ==2011]['Prevalence'].mean()
data_prev[data_prev['Year'] ==2012]['Prevalence'].mean()


year_avg2011 =data_prev[data_prev['Year'] ==2011]['Prevalence'].mean()
year_avg2011
new_list.append(year_avg2011)

year_avg2012 =data_prev[data_prev['Year'] ==2012]['Prevalence'].mean()
year_avg2012
new_list.append(year_avg2012)


new_list