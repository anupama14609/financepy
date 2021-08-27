from bs4 import BeautifulSoup
import requests
import lxml
import pickle


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', attrs={'class':'wikitable sortable'})

    tickers = []

    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text.replace('\n','').strip()
        tickers.append(ticker)

    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

save_sp500_tickers()


