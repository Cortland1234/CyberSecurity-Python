'''
Assignment 3 Help

'''

import os
import hashlib

DIR = 'FILES'

fileHashes = {}

for root, dirs, files in os.walk(DIR):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        print(fullPath)
        with open(fullPath, 'rb') as fileObj:
            fileContent = fileObj.read()
            sha256Obj = hashlib.sha256()
            sha256Obj.update(fileContent)
            hexDigest = sha256Obj.hexdigest()
            print(hexDigest)
        
        # At this point you need to hash the
        # the contents of each file
        

        
        
