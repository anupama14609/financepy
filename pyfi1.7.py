import pandas as pd 
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')
df = pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)

print(df)
df.plot()
plt.show()

print(df['Adj Close'])
df['Adj Close'].plot()
plt.show()

print(df[['Open','High']])
df[['Open','High']].plot()
plt.show()


