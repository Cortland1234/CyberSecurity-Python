'''
Copyright (c) 2019 Python Forensics

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.
'''
from __future__ import print_function

# Using the Python Hashing Module

# Importing Modules

import os           # Std Lib OS Module
import hashlib      # Std Lib Hashing Module

# Read current directory contents
# into a list

filesToHash = os.listdir(".")

# Loop through each file
for eachFile in filesToHash:
    # Validate that the each entry is
    # a file (i.e. not a directory or link)
    # and we have proper rights to read the file
    if os.path.isfile(eachFile):
        if os.access(eachFile, os.R_OK):
            try: 
                # Attempt to open the file
                with open(eachFile, "rb") as theFile:
                    # Create a new hashing object
                    hashObj = hashlib.sha256()
                    # Now read in the file in chunks
                    # and hash each chunk
    
                    chunkSize = 2**16
                    
                    while True:
                        chunk = theFile.read(chunkSize)
                        # if we still have data
                        # keep updating the hash
                        if len(chunk) > 0:
                            hashObj.update(chunk)
                        # otherwise we are finished hashing
                        else:
                            print(eachFile, hashObj.hexdigest())
                            break
            except:
                print(eachFile, "Hashing Failed")
        else:
            print(eachFile, "Not Readable")
    else:
        print(eachFile, "Not a File")

