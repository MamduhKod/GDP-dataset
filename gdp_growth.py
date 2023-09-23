import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gdp_growth.csv')
data = data.set_index('Country Name')
data = data.T
data = data.iloc[30:]
data

# map the growth of countries GDP for last 20 years

plt.figure = figsize=((100,50))
plt.plot(data.index, data.columns,color='b',label='GDP')
plt.xlabel("Year")
plt.ylabel("GDP")
plt.title('GDP per country')