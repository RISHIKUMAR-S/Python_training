import requests
from bs4 import BeautifulSoup

# Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
#print(page.text)
soup = BeautifulSoup(page.content, 'lxml')
#print(soup)
# Extract title of page
page_title = soup.title.text

# print the result
print(soup)
print(page_title)