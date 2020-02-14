import requests
import time
from bs4 import BeautifulSoup

allRecipes_links = []

baseLink = "https://www.allrecipes.com/?page={}"


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # recipeTags = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    # recipeTags = soup.find_all("a", {"class": "js-quick-basket-title"})  # <class 'bs4.element.ResultSet'>
    # recipeTags = soup.find_all("a").get('href')
    # recipeTags = soup.find_all("div", {"class": "fixed-recipe-card__info"})
    # recipeTags = soup.find_all("a", {"class": "fixed-recipe-card__title-link"})

    for link in soup.find_all("a", {"class": "fixed-recipe-card__title-link"}):
        allRecipes_links.append(link.get('href'))

    # return allRecipes_links

for i in range(1, 10):  # max page = 5
    getlinks(i)
    time.sleep(2)

print(allRecipes_links)

with open('allRecipes_links.txt', 'w+') as f:
    for recipes in allRecipes_links:
        f.write('%s\n' % recipes)