import requests
import time
from bs4 import BeautifulSoup

food52_links = []
baseLink = 'https://food52.com/recipes/search?o=rating&page={}&tag=test-kitchen-approved'


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # recipeTags = [a['href'] for a in soup.findAll("div", {"class": "card__details"}) if a.text]  # <class 'bs4.element.ResultSet'>
    # recipeTags = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    # recipeTags = soup.find_all("a", {"class": "js-quick-basket-title"})  # <class 'bs4.element.ResultSet'>
    # recipeTags = soup.find_all("a").get('href')
    for link in soup.find_all("a", {"class": "js-quick-basket-title"}):
        food52_links.append("https://food52.com" + link.get('href'))
    return food52_links


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

print(food52_links)

with open('food52_links.txt', 'w+') as f:
    for recipes in food52_links:
        f.write('%s\n' % recipes)  # splitting each wod/item into a separate row