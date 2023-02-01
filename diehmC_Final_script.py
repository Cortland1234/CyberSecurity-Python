import nltk
nltk.download('punkt')
#Punkt is an nltk library module that allows us to tokenize large texts, and this is used in the project 
#to get words from the text. SOURCE INFO: https://www.nltk.org/api/nltk.tokenize.punkt.html
nltk.download('averaged_perceptron_tagger')
#Perceptron Tagger is another nltk library module that allows us to tag words that fit a certain category
#In this project, it is used to tag the nouns and verbs. SOURCE INFO: https://www.nltk.org/api/nltk.tag.perceptron.html 
import re
from bs4 import BeautifulSoup
import requests
import nltk
from string import punctuation


#====================================================
#GETTING WEB PAGE TEXT WITH BEAUTIFULSOUP
#====================================================
url = 'https://casl.website/'
page = requests.get(url)
soupObject = BeautifulSoup(page.text, 'html.parser')


print(f"\n\nPROCESSING DATA FROM \"{url}\"....\n\nPROCESSING DATA FROM \"{url}\"....\n\nPROCESSING DATA FROM \"{url}\"....")
#====================================================
#GETTING ALL UNIQUE URLS
#====================================================

def filterURL(text):
    filtered_text = []
    for words in text:
        if words.has_attr("href"):
            filtered_text.append(words)
    return filtered_text

def mapUrlData(ftext, url):
    for words in range(len(ftext)):
        if "http" in ftext[words]["href"]:
            ftext[words] =  ftext[words]["href"]  
        else:
            ftext[words] = url + ftext[words]["href"][1:] 
#These functions filter the data by its attribute ("href"). The words that have "href" as an attribute are appended to a list,
#which is then mapped by mapUrlData

filteredURL = filterURL(soupObject.findAll("a"))
mapUrlData(filteredURL, url)
uniqUrls = set(filteredURL)

#====================================================
#GETTING ALL UNIQUE IMAGE URLS
#====================================================

def filterImg(text):
    filtered_text = []
    for words in text:
        if words.has_attr("src"):
            filtered_text.append(words)
    return filtered_text

def mapImgData(ftext, url):
    for words in range(len(ftext)):
        if "http" in ftext[words]["src"]:
            ftext[words] =  ftext[words]["src"]  
        else:
            ftext[words] = url + ftext[words]["src"][1:] 
#These functions are the same as the ones for the URLs, but these filter by "src" instead

filteredImg = filterImg(soupObject.findAll("img"))
mapImgData(filteredImg, url)
uniqImages = set(filteredImg)

#====================================================
#GETTING ALL PHONE NUMBERS THAT MATCH THE REGEX
#====================================================
phNumbers = re.search(r"\(?\d{3}\)?-? *\d{3}-? *-?\d{4}",soupObject.text).group()

#====================================================
#GETTING ALL EMAIL ADDRESSES MATCH THE REGEX
#====================================================
emailAddresses = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",soupObject.text).group()

#====================================================
#GETTING ALL ZIP CODES THAT MATCH THE REGEX
#====================================================
zipCodes = re.search(r"\d{5}(?:-\d{4})?",soupObject.text).group()

#====================================================
#GETTING ALL TEXT FROM ALL PAGES
#====================================================
pageText = soupObject.find("body").text
#This is searching the soupObject for the HTML "body"
for url in uniqUrls:
  page = requests.get(url)
  soupObject = BeautifulSoup(page.text, 'html.parser')
  pageText = (pageText + soupObject.find("body").text)
#This loop is iterating through all unique URLs, finding the "body" contents, and adding them to pageText

#====================================================
#GETTING ALL (UNIQUE) VOCABULARY WORDS
#====================================================
puncWords = list(punctuation)
#puncWords is using the imported punctuation library to make a list of punctuation. This punctuation is discarded as vocabulary below
vocab= set([word.lower() for word in nltk.word_tokenize(pageText) if word not in puncWords and word.isalpha() and len(word)>1])
#This is creating a list of all unique vocabulary words. The words are converted to lowercase and are not added to the list if the word is also in puncWords
#The word is also only added if it is a non-number, and if the length of the word is >1.
#====================================================
#GETTING ALL (UNIQUE) NOUNS
#====================================================

taggedWords = nltk.pos_tag(vocab)
nouns = set(filter(lambda x:x[1].startswith("N"), taggedWords)) 
#This is filtering each word into nouns and non-nouns. It filters by the nltk pos_tag, 
#and if the tag is "N" then it is a noun

#====================================================
#GETTING ALL (UNIQUE) VERBS
#====================================================
verbs = set(filter(lambda x:x[1].startswith("V"), taggedWords))
#This is filtering each word into verbs and non-verbs. It filters by the nltk pos_tag, 
#and if the tag is "V" then it is a noun

#====================================================
#WRITING DATA TO THE REPORT
#====================================================

with open("diehmC_Final_Report.txt","w") as outReport:
#Creating new file for the report

    outReport.write("CORTLAND DIEHM\nDR. ALHARTHI\nCYBV 473\n12/5/2022\nFINAL SCRIPTING PROJECT")

    outReport.write("\n\n====================\nUNIQUE WEBPAGE URLS\n====================\n")
    for url in uniqUrls:
        outReport.write(f"{url}\n")
#Writing all URLS

    outReport.write("\n\n====================\nUNIQUE IMAGE URLS:\n====================\n")
    for image in uniqImages:
        outReport.write(f"{image}\n")
#Writing all Image URLS

    outReport.write("\n\n====================\nPHONE NUMBERS:\n====================\n")
    outReport.write(phNumbers)
#Writing all Phone Numbers

    outReport.write("\n\n====================\nEMAIL ADDRESSES:\n====================\n")
    outReport.write(emailAddresses)
#Writing all Email Addresses

    outReport.write("\n\n====================\nZIP CODES:\n====================\n")
    outReport.write(zipCodes)
#Writing all Zip Codes    

    outReport.write("\n\n====================\nUNIQUE VOCABULARY WORDS:\n====================\n")
    for word in vocab:
        outReport.write(f"{word}\n")
#Writing all Vocabulary        

    outReport.write("\n\n====================\nPOSSIBLE UNIQUE NOUNS:\n====================\n")
    for noun in nouns:
        outReport.write(f"{noun[0]}\n")
#Writing all Nouns        
    
    outReport.write("\n\n====================\nPOSSIBLE UNIQUE VERBS:\n====================\n")
    for verb in verbs:
        outReport.write(f"{verb[0]}\n")
#Writing all Verbs

    outReport.write("\n\nEND OF REPORT!")        
  

print("\nREPORT HAS BEEN CREATED UNDER THE NAME \"diehmC_Final_Report.txt\"!\n\nSHUTTING DOWN PROGRAM...\nGOODBYE\n")

