from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr") 
print("\nAll Rows Of Table================================\n")
print(gdp_table_data)

print("\nFirst Row Of Table================================\n")
print(gdp_table_data[0])

