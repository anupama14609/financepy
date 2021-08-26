import pandas as pd
import matplotlib.dates as mdat

df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head())
print(df_volume.head())

