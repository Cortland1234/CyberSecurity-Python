'''
Week Five Assignment #9
'''

'''
Cortland Diehm

Dr. Alharthi

10/4/2022
'''

import requests
import sys

from bs4 import BeautifulSoup

page = requests.get("https://casl.website/")

soup = BeautifulSoup(page.text, "html.parser")

f = open("diehmC_WK6_output.txt", "w")

f.write("TITLE: ")
f.write("\n")

for x in soup.find_all("title"):
    f.write(x.get_text())

f.write("\n\n")
f.write("URL LIST: ")
f.write("\n")

urlList = []

for j in soup.find_all("a"):
    url = j.get("href")
    urlList.append(url)

for word in urlList:
    if word != None and word.startswith("http"):
        f.write(word)
        f.write("\n")
    else:
        continue

f.write("\n")
f.write("IMAGES: ")
f.write("\n")

images = soup.find_all("img")

for eachImage in images:
    imgURL = eachImage['src']
    f.write(imgURL)
    f.write("\n")

f.write("\n\n")
f.write("END OF SCRIPT")

f.close()
