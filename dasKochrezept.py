import requests
import time
from bs4 import BeautifulSoup

dasKochrezept_links = []
baseLink = "https://www.daskochrezept.de/suche?search=%20&page={}"


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "teaser-search-result__title"}):
        dasKochrezept_links.append("https://www.daskochrezept.de" + link.get('href'))


for i in range(1, 11):
    getlinks(i)
    time.sleep(2)

with open('dasKochrezept_links.txt', 'w+') as f:
    for recipes in dasKochrezept_links:
        f.write('%s\n' % recipes)