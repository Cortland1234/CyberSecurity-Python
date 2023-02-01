'''
Hash File Functions and usage example
'''

import hashlib
import sys

    
def HashFile(filePath):
    ''' 
        function takes one input a valid filePath
        returns the hexdigest of the file
        or error 
    '''
    try:
        with open(filePath, 'rb') as fileToHash:
            fileContents = fileToHash.read()
            hashObj = hashlib.md5()
            hashObj.update(fileContents)
            digest = hashObj.hexdigest()
            return digest
    except Exception as err:
        return str(err)
        
print("Hash File Function Demonstration")

fileName = input("Enter file to hash: ")

hexDigest = HashFile(fileName)
print(hexDigest)
