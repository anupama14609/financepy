from bs4 import BeautifulSoup
import pickle
import requests
import lxml

resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text,"lxml")

titlev1 = soup.find('title')
titletxtv1 = soup.find('title').text
print("Title Version 1: {}".format(titlev1))
print("Title Version 1 Text: {}".format(titletxtv1))

titlev2 = soup.title
titletxtv2 = soup.title.text
print("Title Version 2: {}".format(titlev2))
print("Title Version 2 Text: {}".format(titletxtv2))

