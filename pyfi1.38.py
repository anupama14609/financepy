import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def visualize_data():
    style.use('ggplot')
    df = pd.read_csv('sp500_joined_closes.csv')
    df.corr()
    plt.plot()
    plt.show()


visualize_data()