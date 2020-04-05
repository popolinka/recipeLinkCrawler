import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

bonAppetit_links = []

browser = webdriver.Chrome()
browser.get("https://www.bonappetit.com/recipes")
# scrollDown = browser.execute_script("window.scrollTo(0, document.body.scrollHeight  )")
time.sleep(5)

cookie_Accept = browser.find_element_by_id('onetrust-accept-btn-handler')
cookie_Accept.click()

more_button = browser.find_element_by_class_name("btn-more-channel")

for x in range(1, 14):
    more_button.click()
    time.sleep(5)

html_source = browser.page_source
browser.close()

soup = BeautifulSoup(html_source, "html.parser")
data = html_source.encode('utf-8')

for link in soup.find_all("a", {"class": "button-2d"}):
    bonAppetit_links.append("https://www.bonappetit.com/" + link.get('href'))

print(bonAppetit_links)

with open('bonAppetit_links.txt', 'w+') as f:
    for recipes in bonAppetit_links:
        f.write('%s\n' % recipes)
