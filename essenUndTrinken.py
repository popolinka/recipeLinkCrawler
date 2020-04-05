import requests
import time
from bs4 import BeautifulSoup
import re

essenUndTrinken_links = []
baseLink = "https://www.essen-und-trinken.de/rezepte/archiv?page={}"


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    parent = soup.find_all("div", {"class": "headline-group-inside"})

    for divs in parent:
        for link in divs.find_all("a"):
            # essenUndTrinken_links.append(link.get("href"))
            if re.search("\A/rezepte", link.get('href')):  # removing additional useless stuff
                essenUndTrinken_links.append("https://www.essen-und-trinken.de" + link.get('href'))
            else:
                pass


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

# print(essenUndTrinken_links)

with open('essenUndTrinken_links.txt', 'w+') as f:
    for recipes in essenUndTrinken_links:
        f.write('%s\n' % recipes)
