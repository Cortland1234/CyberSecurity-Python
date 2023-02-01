'''
Hash File Functions and usage example
'''
from __future__ import print_function
import hashlib
import sys

''' Determine which version of Python '''
if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False
    
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

if PYTHON_2:
    fileName = raw_input("Enter file to hash: ")
else:
    fileName = input("Enter file to hash: ")

hexDigest = HashFile(fileName)
print(hexDigest)
