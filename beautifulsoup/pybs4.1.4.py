from bs4 import BeautifulSoup
import requests
import lxml

html_content = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
soup = BeautifulSoup(html_content.text, "lxml")
link  = soup.find('a')
linktext = soup.find('a').text

print(f"First Link of Web Page :{link}")
print(f"First Link Text of Web Page:{linktext}")


