from bs4 import BeautifulSoup
import requests
import lxml

html_content = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
soup = BeautifulSoup(html_content.text, "lxml")
thumb  = soup.find('div',{'class':'thumb tright'})
thumbtext  = soup.find('div',{'class':'thumb tright'}).text
thumbinner  = soup.find('div',{'class':'thumbinner'})
thumbinnertext  = soup.find('div',{'class':'thumbinner'}).text

print("\nFinding Div================================\n")
print(thumb)
print("\nFinding Div Text================================\n")
print(thumbtext)

print("\nFinding Inner Div================================\n")
print(thumbinner)
print("\nFinding Inner Div Text================================\n")
print(thumbinnertext)


