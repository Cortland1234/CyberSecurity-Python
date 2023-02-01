
'''
Week Two Assignment 2 - File Hashing

Cortland Diehm
9/5/2022
'''

'''
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Using the os library and the os.walk() method 
   a) Create a list of all files
   b) Create an empty dictionary named fileHashes 
   c) Iterate through the list of files and
      - calculate the md5 hash of each file
      - create a dictionary entry where:
        key   = md5 hash
        value = filepath
    d) Tterate through the dictionary
       - print out each key, value pair
    
3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK1_script.py
                 alharthiD_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os
import hashlib

directory = "."

hashList = []
fileList   = []
fileHashes = {}

for root, dirs, files in os.walk(directory):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        fileList.append(fullPath)
    
        with open(fullPath, 'rb') as fileObj:
            fileContent = fileObj.read()
            sha256Obj = hashlib.sha256()
            sha256Obj.update(fileContent)
            hexDigest = sha256Obj.hexdigest()
            hashList.append(hexDigest)
    
    for key in hashList:
        for value in fileList:
            fileHashes[key] = value
            fileList.remove(value)
            break
    for key,value in fileHashes.items():
        print(key, value)
        

                 

        
        
