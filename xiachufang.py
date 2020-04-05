import requests
import time
import re
from bs4 import BeautifulSoup

xiachufang_links = []
baseLink = "https://www.xiachufang.com/explore/?page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    parent = soup.find_all("div", {"class": "info pure-u"})
    for divs in parent:
        for link in divs.find_all("a"):
            if re.search("\A/recipe", link.get('href')):  # removing additional useless stuff
                xiachufang_links.append("https://www.xiachufang.com" + link.get('href'))
            else:
                pass


for i in range(1, 10):
    getlinks(i)
    time.sleep(2)

with open('xiachufang_links.txt', 'w+') as f:
    for recipes in xiachufang_links:
        f.write('%s\n' % recipes)

