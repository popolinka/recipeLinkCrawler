import requests
import time
from bs4 import BeautifulSoup

lecker_Links = []
baseLink = "https://www.lecker.de/tagesrezept/archiv/page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "teaser teaser--full-2col box w-6"}):
        lecker_Links.append(link.get('href'))

    # return allRecipes_links


for i in range(1, 10):  # max page = 5
    getlinks(i * 3)  # chefkoch increases 30 60 90 ...
    time.sleep(2)

print(lecker_Links)

with open('lecker_Links.txt', 'w+') as f:
    for recipes in lecker_Links:
        f.write('%s\n' % recipes)