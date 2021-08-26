from bs4 import BeautifulSoup
import pickle
import requests
import lxml

resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text,"lxml")
pretisoup = soup.prettify() 
print(pretisoup)

titlev1 = soup.title
titlev2 = soup.find('title')
print(titlev1)
print(titlev2)

titletxtv1 = soup.title.text
titletxtv2 = soup.find('title').text
print(titletxtv1)
print(titletxtv2)

