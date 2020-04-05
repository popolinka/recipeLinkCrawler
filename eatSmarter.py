import requests
import time
from bs4 import BeautifulSoup

eatSmarter_links = []
baseLink = "https://eatsmarter.com/search/recipes?page={}"


def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "teaser-wrapper-link"}):
        eatSmarter_links.append("https://eatsmarter.com" + link.get('href'))


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

# print(eatSmarter_links)

with open('eatSmarter_links.txt', 'w+') as f:
   for recipes in eatSmarter_links:
       f.write('%s\n' % recipes)