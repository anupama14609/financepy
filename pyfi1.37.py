import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def visualize_data():
    style.use('ggplot')
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    column_labels = df_corr.columns 
    row_labels = df_corr.index 

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)

    plt.plot()
    plt.show()


visualize_data()