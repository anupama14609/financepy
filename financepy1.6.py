import pandas as pd 
from matplotlib import style
import matplotlib.pyplot as plt

style.use('ggplot')
df = pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)

df[['Open','High']].plot()
plt.show()


