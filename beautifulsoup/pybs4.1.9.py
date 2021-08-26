from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

headings = []
for th in gdp_table_data[0].find_all("th"):
    headings.append(th)

print("\nHeadings Elements of First Row Of Table================================\n")
print(headings)
