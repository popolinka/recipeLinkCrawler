import requests
import time
from bs4 import BeautifulSoup

lecker_Links = []
baseLink = "https://www.lecker.de/tagesrezept/archiv/page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    parent = soup.find_all("div", {"class": "teaser teaser--full-2col box w-6"})
    for divs in parent:
        for link in divs.find_all("a"):
            lecker_Links.append("https://www.lecker.de" + link.get('href'))


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)


with open('lecker_Links.txt', 'w+') as f:
    for recipes in lecker_Links:
        f.write('%s\n' % recipes)