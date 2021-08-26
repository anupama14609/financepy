from bs4 import BeautifulSoup
import requests
import lxml

html_content = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
soup = BeautifulSoup(html_content.text, "lxml")

for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))



