'''
Extract simple data from a webpage
using Python Standard Libary requests
Exp-14.py
by Chet Hosmer
'''

# Python Standard Libaries
import requests    # Python Standard Library for url requests

page = requests.get('http://python.org/')   # retrieve web-page
print(page.text)

print('\n\nEnd Script')

