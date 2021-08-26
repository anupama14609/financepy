from bs4 import BeautifulSoup
import pickle
import requests
import lxml

resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text,"lxml")
pretisoup = soup.prettify() 
print(pretisoup)

