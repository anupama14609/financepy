from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows
print("\n0th Row Of Table================================\n")
print(gdp_table_data[0])

print("\nTable Headings Sup Element================================\n")
suptag = []
for sup in gdp_table_data[0].find_all("sup"):
    suptag.append(sup)
print(suptag)

print("\nTable Headings Sup Element Text================================\n")
suptagtext = []
for sup in gdp_table_data[0].find_all("sup"):
    suptagtext.append(sup.text)
print(suptagtext)
