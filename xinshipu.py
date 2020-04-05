import requests
import time
import re
from bs4 import BeautifulSoup

xinshipu_links = []
baseLink = "https://www.xinshipu.com/xinshipu/?page={}"

def getlinks(pageNum):
    url = baseLink.format(pageNum)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", {"class": "no-overflow"}):
        xinshipu_links.append("https://www.xinshipu.com" + link.get('href'))

    # parent = soup.find_all("div", {"class": "info pure-u"})
    # for divs in parent:
    #     for link in divs.find_all("a"):
    #         if re.search("\A/recipe", link.get('href')):  # removing additional useless stuff
    #             xinshipu_links.append("https://www.xiachufang.com" + link.get('href'))
    #         else:
    #             pass


for i in range(1, 11):
    getlinks(i)
    time.sleep(2)

with open('xinshipu_links.txt', 'w+') as f:
    for recipes in xinshipu_links:
        f.write('%s\n' % recipes)



