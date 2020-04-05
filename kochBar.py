import requests
import time
from bs4 import BeautifulSoup

kochBar_links = []
baseLink = "https://www.kochbar.de/rezepte/alle-rezepte.html?page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "kb-teaser-list-link"}):
        kochBar_links.append(link.get('href'))


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

with open('kochBar_links.txt', 'w+') as f:
    for recipes in kochBar_links:
        f.write('%s\n' % recipes)
