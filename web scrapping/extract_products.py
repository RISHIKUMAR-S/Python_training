"""Farfetch products web scrapper
This script parses the farfetch website products and stores the scrapped prodcucts in a csv file.

How to execute:
1. Make sure you have python 3.9 or above installed in your machine.
2. Execute below command to install the required dependencies.
pip install -r requirements.txt
3. execute the script
python extract_products.py

This creates below 2 csv files with the products.
1. farfetch_men.csv
2. farfetch_women.csv
"""

from csv import writer
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.farfetch.com"
USER_AGENT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
CATEGORY_MEN = "141259"
CATEGORY_WOMEN = "141258"
CLASS_NAME_PRODUCT = "ltr-x69rqn"
CLASS_NAME_BRAND = "ltr-17q7kb6-Body-BodyBold"
CLASS_NAME_DESCRIPTION = "e1s5vycj0"
CLASS_NAME_PRICE = "e15nyh750"
CLASS_NAME_SIZES = "ek9vc7i0"
CLASS_NAME_DETAIL_LINK = "ltr-1gxq4h9"
OUT_FILE_MEN = "farfetch_men.csv"
OUT_FILE_WOMEN = "farfetch_women.csv"
OUT_HEADERS = ['Brandname', 'Description', 'Price', 'Url', 'Sizes']


def extract_products(category, output_filename):
    """Gets the product list from the web content

    Parameters
    ----------
    category : str
        Id of the category listed in the website
    output_filename : str
        Name of the csv file which stores the products data
    """
    products_html_elements = get_products_html_elements(category)
    products = get_products(products_html_elements)
    write_products(products, output_filename)

def get_products_html_elements(category):
    """Gets the web content with the beautifulsoup wrapper as list of product html tags

    Parameters
    ----------
    category : str
        Id of the category listed in the website

    Returns
    ----------
    list
        a collection of products html which has same tag name and class name
    """
    url = f"{BASE_URL}/in/sets/new-in-this-week-eu-men.aspx?page=1&view=90&sort=3&category={category}"
    page = requests.get(url, headers=USER_AGENT_HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find_all('div', class_=CLASS_NAME_PRODUCT)

def get_product_attribute(product_html, classname):
    """Extracts the product attribute fromthe product html using the given class name

    Parameters
    ----------
    product_html : str
        Html content of the product
    classname : str
        Class name of the attribute

    Returns
    ----------
    str
        product attribute (ex: Blue)
    """
    return product_html.find("p", class_=classname).text

def get_product_link(product_html, classname):
    """Extracts the proudct detail link from the given prouct html using the given classname

    Parameters
    ----------
    product_html : object
        Html content of the product
    tag : str
        Name of the attribute tag (ex: color)
    classname : str
        Class name of the tag which has the content

    Returns
    ----------
    str
        link stored inside the tag
    """
    return product_html.find("a", class_=classname).get('href')

def write_products(products, output_filename):
    """Write the data in a csv file

    Parameters
    ----------
    products : list
        Contains the each data of the products in list
    output_filename : str
        Name of the csv file which stores the products data

    """
    with open(output_filename, 'w', encoding='utf8', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(OUT_HEADERS)  # To write heading into the file row wise
        for product in products:
            csv_writer.writerow(product)

def get_products(products_html_elements):
    """Creates a list by extrating each data from the html

    Parameters
    ----------
    products_html_elements : object
        a collection of products html which has similar tag and class name

    Returns
    ----------
    list
        Contains the each data of the products in list
    """
    products = []
    for product_html in products_html_elements:
        brand_name = get_product_attribute(
            product_html, CLASS_NAME_BRAND)
        description = get_product_attribute(product_html, CLASS_NAME_DESCRIPTION)
        price = get_product_attribute(product_html, CLASS_NAME_PRICE)
        sizes = get_product_attribute(product_html, CLASS_NAME_SIZES)
        link = BASE_URL + get_product_link(product_html, CLASS_NAME_DETAIL_LINK)
        products.append([brand_name, description, price, link, sizes])
    return products

extract_products(CATEGORY_MEN, OUT_FILE_MEN)
extract_products(CATEGORY_WOMEN, OUT_FILE_WOMEN)