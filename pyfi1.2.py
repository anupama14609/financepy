import datetime
import matplotlib.pyplot as plt 
import pandas_datareader.data as web 
from matplotlib import style

style.use('ggplot')

df = web.DataReader('GOOGL', 'yahoo')
df.head()
print(df.head())
print(df.tail())



                   