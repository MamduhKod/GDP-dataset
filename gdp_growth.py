import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gdp_growth.csv')

data = data[1:10]
data.drop(columns='Code')
data.fillna(0)
data

plt.figure(figsize=(15,5))
plt.plot(data['Country Name'], data['2012'],color='b',label='GDP')
plt.xlabel("Country")
plt.ylabel("GDP")
plt.title('GDP per country')