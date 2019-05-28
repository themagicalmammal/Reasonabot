import bs4
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
driver.get('https://www.mysmartprice.com/msp/search/search.php?search_type=auto&typed_term=poco&s=poco%20f1#s=poco%20f1')
res = driver.execute_script("return document.documentElement.outerHTML")
soup = bs4.BeautifulSoup(res , 'html.parser')
driver.quit()

containers = soup.findAll('div',{'class':'prdct-item'})
#print(containers)

productnames = []
links=[]
for items in containers:
    productname = items.find('a' , {"class" : "prdct-item__name"}).text
    productnames.append(productname[1:-1])
    links.append(items.a["href"])
print(productnames)
print(links)