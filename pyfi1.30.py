import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

def visualize_data():
    style.use('ggplot')
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()
    data = df_corr.values
    print(data)


visualize_data()