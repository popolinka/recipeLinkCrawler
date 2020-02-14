import requests
import time
from bs4 import BeautifulSoup

chefKoch_Links = []
baseLink = "https://www.chefkoch.de/rs/s{}0/Rezepte.html"  # s30 60 90 120...


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # recipeTags = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    # recipeTags = soup.find_all("a", {"class": "js-quick-basket-title"})  # <class 'bs4.element.ResultSet'>
    # recipeTags = soup.find_all("a").get('href')
    # recipeTags = soup.find_all("div", {"class": "fixed-recipe-card__info"})
    # recipeTags = soup.find_all("a", {"class": "fixed-recipe-card__title-link"})

    for link in soup.find_all("a", {"class": "ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item"}):
        chefKoch_Links.append(link.get('href'))

    # return allRecipes_links


for i in range(1, 6):  # max page = 5
    getlinks(i * 3)  # chefkoch increases 30 60 90 ...
    time.sleep(2)

print(chefKoch_Links)

with open('chefKoch_Links.txt', 'w+') as f:
    for recipes in chefKoch_Links:
        f.write('%s\n' % recipes)