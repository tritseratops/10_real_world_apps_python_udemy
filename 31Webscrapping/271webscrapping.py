import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})


c= r.content

soup = BeautifulSoup(c, "html.parser")

cities_elements = soup.find_all("div", {"class":"cities"})





for city in cities_elements:
    city_name = city.find_all("h2")[0].text
    city_paragraph = city.find_all("p")[0].text
    print(city_name)
    print(city_paragraph)