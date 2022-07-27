from pandas import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup

opt = ChromeOptions()
opt.headless = True
driver = webdriver.Chrome(r"C:\Users\Rishi\Desktop\chromedriver.exe",options=opt)
#navigate to the url
driver.get("https://www.farfetch.com/in/sets/new-in-this-week-eu-men.aspx?page=1&view=90&sort=3&category=141259")
content = driver.page_source
soup = BeautifulSoup(content)
products = []
BASE_URL = "https://www.farfetch.com"

def get_product_attribute(product_html, tag, classname):
    return product_html.find(tag, class_=classname).text

def get_product_link(product_html, tag, classname):
    return product_html.find(tag, class_=classname).get('href')

for product_html in soup.find_all('div', class_="ltr-x69rqn"):
    brand_name = get_product_attribute(product_html, 'p', "ltr-17q7kb6-Body-BodyBold")
    description = get_product_attribute(product_html, 'p', "e1s5vycj0")
    price = get_product_attribute(product_html, 'p', "e15nyh750")
    sizes = get_product_attribute(product_html, 'p', "ek9vc7i0")
    link = BASE_URL + get_product_link(product_html, "a", "ltr-1gxq4h9")
    products.append([brand_name, description, price, link, sizes])

'''
driver.get("https://www.farfetch.com/in/shopping/men/balmain-monogram-jacquard-baseball-cap-item-17923229.aspx?storeid=13537")
content = driver.page_source
soup = BeautifulSoup(content)

productid = get_product_attribute(soup, 'span', "_b4693b")

print(products)
print(productid)
'''
#close the browser
driver.close()