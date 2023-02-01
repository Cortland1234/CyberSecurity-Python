'''
Scripting Assignment #6: Extract Metadata from Digital Images

Name: Cortland Diehm
Date: September 18, 2022
Professor: Alharthi
'''

'''
Utilizing the Python Image Library (PIL) and the examples provided during this weeks lecture develop a Python script that accurately identifies digital images.

Extract the testimages provided into the Virtual Desktop Environment (in the persistent storage areas)

Develop a script that:

1) Prompts the user for a directory path to search

2) Verify that the path provided exists and is a directory

3) Iterate through each file in that directory and examine it using PIL.

4) Generate a prettytable report of your search results (sample shown here)
'''
import os
from PIL import Image
from prettytable import PrettyTable

imgTable = PrettyTable(["Image?","File","FileSize","Ext","Format","Width","Height","Mode"])

valid = False

while not valid:
    path = input("Enter a directory to search: ")

    if os.path.isdir(path):
        valid = True
        imageFiles = []
        for root, directories, filenames in os.walk("."):
            for name in filenames:
                imageFiles.append(os.path.join(root, name))
    else:
        print("Invalid input. No such directory.")

for f in imageFiles:
    lPath = os.path.join(f)
    absolutePath = os.path.abspath(lPath)
    ext = os.path.splitext(absolutePath)[1]
    size = os.path.getsize(absolutePath)
    fileSize = "{:,}".format(size)

    try:
        with Image.open(absolutePath) as image:
            imageStatus = "YES"
            imageFormat = image.format
            imageMode = image.mode
            imageWidth = image.size[0]
            imageHeight = image.size[1]

            imgTable.add_row([imageStatus, lPath, fileSize, ext, imageFormat, imageWidth, imageHeight, imageMode])
    except:
        continue

print(imgTable)