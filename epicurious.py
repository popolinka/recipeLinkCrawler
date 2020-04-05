import requests
import time
from bs4 import BeautifulSoup

epicurious_links = []
baseLink = "https://www.epicurious.com/search?content=recipe&page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "show-quick-view"}):
        epicurious_links.append("https://www.epicurious.com" + link.get('href'))


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

with open('epicurious_links.txt', 'w+') as f:
    for recipes in epicurious_links:
        f.write('%s\n' % recipes)