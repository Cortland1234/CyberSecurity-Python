'''
Extract simple data from a webpage
using beautifulsoup
Exp-15.py
by Chet Hosmer
'''

# Python Standard Libaries
import requests                         # Python Standard Library for url requests

# Python 3rd Party Libraries
from bs4 import BeautifulSoup           # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4

page = requests.get('https://python.org')      # retrieve a page from your favorite website

soup = BeautifulSoup(page.text, 'html.parser') # convert the page into a beautifulsoup object for processing

images = soup.findAll('img')

for eachImage in images:
    imgURL = eachImage['src']
    print(imgURL)                   # display the url of the image
    print(eachImage['alt'])         # display the alternate text associated with the image
    print()

print('\n\nScript Complete')

