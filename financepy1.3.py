import datetime
import matplotlib.pyplot as plt 
import pandas_datareader.data as web 
from matplotlib import style

style.use('ggplot')
start = datetime.datetime(2012,12,31)
end = datetime.datetime(2016,12,31)
df = web.DataReader('GOOGL', 'yahoo', start,end)
df.head()
print(df.head())
print(df.tail())



                   