import bs4
import random
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
driver.get('https://www.brainyquote.com/top_100_quotes')
res = driver.execute_script("return document.documentElement.outerHTML")
soup = bs4.BeautifulSoup(res , 'lxml')
driver.quit()

containers = soup.findAll('a')
qt = []
for items in containers:
    qt.append(items.text)

qt = qt[80:146]

quotes = []
authors = []
i=0
while i < len(qt)-1:
    if i%2 == 0:
        quotes.append(qt[i])
        authors.append(qt[i+1])
    i += 1

quotesauth = []
ranc = random.randint(1,len(quotes)-1)

sam = ""
i = 0
while i < len(quotes) - 1:
    sam = quotes[i] + " - " + authors[i]
    quotesauth.append(sam)
    i += 1
print(quotesauth[ranc])