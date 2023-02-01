'''
Week Five Assignment #7
'''

'''
Cortland Diehm

Dr. Alharthi

9/26/2022
'''


import sys
import re
from binascii import hexlify 
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE =  4096

# regular expressions

ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')  
uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')

# Create empty lists
emailList = []
urlList = []

# Read in the binary file test.bin
with open('test.bin', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            emails = ePatt.findall(chunk)
            
            for eachEmail in emails:
                eachEmail = eachEmail.lower()
                eachEmail = eachEmail.decode()
                emailList.append(eachEmail)
        else:
            break

        
with open('memdump.bin', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            urls = uPatt.findall(chunk)
                    
            for eachURL in urls:
                eachURL = eachURL.lower()
                eachURL = eachURL.decode()
                urlList.append(eachURL)
        else:
            break

print("------LIST OF EMAILS------")
for i in emailList:
    print(i)
print("--------------------------")
print("\n")

print("------LIST OF URLS------")
for j in urlList:
    print(j)
print("------------------------")