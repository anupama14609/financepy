import pandas as pd  
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt 
import pandas_datareader.data as web
from matplotlib import style
from bs4 import BeautifulSoup

style.use('ggplot')

start = dt.datetime(2015, 10, 1)
end = dt.datetime.now()

print(start)
print(end)


