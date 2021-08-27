from bs4 import BeautifulSoup
import requests
import lxml
import pickle
import datetime as dt
import os
import pandas_datareader.data as web 

def get_data_from_yahoo():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', attrs={'class':'wikitable sortable'})

    tickers = []

    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text.replace('\n','').strip()
        tickers.append(ticker)

    if not os.path.exists('stock_df'):
        os.makedirs('stock_df')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2020,1,1)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_df/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock_df/{}.csv'.format(ticker))
        else:
            print('Already Exists {}'.format(ticker))

get_data_from_yahoo()


