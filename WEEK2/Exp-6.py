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

# Exploiting the Python OS module

#
# Python Forensics, Inc.

# Importing Modules

import os                   # Std Library OS Module
from time import ctime      # Std Library Time import
                            # just the ctime method

# Examples of some key methods 

# get the current working directory
print("Current Working Directory")
print(os.getcwd())

print("=========================================\n")

# Get the filenames in the current directory
# and store them in a list
print("List of File Names")
fileList = os.listdir(".")

# print(each filename 
for eachFile in fileList:
    print(eachFile)

print("=========================================\n")

# Determine the type of each file in the list
# and print(each type and filename
print("File and Type")
for eachFile in fileList:
    if os.path.isdir(eachFile):
        print("DIR:  ", eachFile)
    elif os.path.isfile(eachFile):
        print("FILE: ", eachFile)
    elif os.path.islink(eachFile):
        print("LINK: ", eachFile)
    elif os.path.ismount(eachFile):
        print("MNT:  ", eachFile)
    else:
        print("UNKNOWN: ", eachFile)
        
print("=========================================\n")
        
# Store the file details in a list
# then sort the resulting list and then
# print the results

print("Store File Details in a List, Sort and Print")
fileDetails = []
for eachFile in fileList:
    if os.path.isdir(eachFile):
        fileDetails.append(["DIR:  ", eachFile])
    elif os.path.isfile(eachFile):
        fileDetails.append(["FILE: ", eachFile])
    elif os.path.islink(eachFile):
        fileDetails.append(["LINK: ", eachFile])
    elif os.path.ismount(eachFile):
        fileDetails.append(["MNT:  ", eachFile])

fileDetails.sort()

for eachItem in fileDetails:
    print(eachItem)

print("=========================================\n")

# Obtain additional file details 
# Store the file details in a list
# then sort the resulting list and print(
# the results

print("Extract additional file details")

fileDetails = []
for eachFile in fileList:
    
    stats = os.stat(eachFile)
    mTime = stats.st_mtime
    mTime = ctime(mTime)
    fSize = stats.st_size
            
    if os.path.isdir(eachFile):
        fileDetails.append(["DIR:  ", eachFile, fSize, mTime])
    elif os.path.isfile(eachFile):
        fileDetails.append(["FILE: ", eachFile, fSize, mTime])
    elif os.path.islink(eachFile):
        fileDetails.append(["LINK: ", eachFile, fSize, mTime])
    elif os.path.ismount(eachFile):
        fileDetails.append(["MNT:  ", eachFile, fSize, mTime])

fileDetails.sort()

for eachItem in fileDetails:
    print(eachItem)

print("=========================================\n")

print("Walk a the Path and print(the relative path")
# Use the os.walk method to walk the path from
# root to bottom

myRoot = "."
for root, dirs, files in os.walk(myRoot):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    # and print(the relative path 
    
    for file in files:
        relativePath = os.path.join(root, file)
        print(relativePath)
        
