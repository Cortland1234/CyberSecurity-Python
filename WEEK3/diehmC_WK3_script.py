from __future__ import print_function
import hashlib
import os
import sys
import time

'''
Assignment 4 - File Processing Object

Cortland Diehm
9/13/2022

Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Create a class named FileProcessor
   a) The Init method shall:
      i) verify the file exists
      ii) Extract key file system metadata from the file
          and store them as instance attribute
          i.e. FilePath, FileSize, MAC Times, Owner, Mode etc.
   b) Create a GetFileHeader Method which will
      i) Extract the first 20 bytes of the header
         and store them in an instance attribute
   c) Create a PrintFileDetails Method which will
      i) Print the metadata
      ii) Print the hex representation of the header
      
3) Demonstrate the use of the new class
   a) prompt the user for a directory path
   b) using the os.listdir() method extract the filenames from the directory path
   c) Loop through each filename and instantiate and object using the FileProcessor Class
   d) Using the object
      i) invoke the GetFileHeader Method
      ii) invoke the PrintFileDetails Method
      
4) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK3_script.py
                 alharthiD_WK3_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''


if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False

class FileProcessor:
    
    def __init__(self, filePath):
        existence = os.path.exists(filePath)
        if existence == False:
            print("File does not exist")        
        else:
            self.filePath = filePath                                  
            self.existence = True                                          
            self.realPath = os.path.realpath(filePath)                   
            self.fileSize = os.path.getsize(filePath)   
            stats = os.stat(self.filePath)
            self.owner = stats.st_uid
            self.mode = stats.st_mode
            self.modifiedTime = time.ctime(os.path.getmtime(filePath))      
            self.accessedTime = time.ctime(os.path.getatime(filePath))      
            self.creationTime = time.ctime(os.path.getctime(filePath))              



    def GetFileHeader(self):
        with open(self.filePath, 'rb') as byteList:
            firstheader = byteList.read(20)
            self.header = firstheader.hex()
            
            
    def PrintFileDetails(self):
        print("=========== File Details ===========")
        print(f"The File Name is: {self.filePath}")
        print(f"Size of File is: {self.fileSize} Bytes")
        print(f"File Mode: {self.mode}")
        print(f"Last Time Modified: {self.modifiedTime}")
        print(f"Time of File Creation: {self.creationTime}")
        print(f"Time of Last Access: {self.accessedTime}")
        print(f"UserID: {self.owner}")
        self.GetFileHeader()
        print(f"File Header is: {self.header}")
        print("=========== End of File ===========")
        
        
inputPath = input("Enter a directory path: ")

names = os.listdir(inputPath)

for x in names:
    fileProc = FileProcessor(x)
    fileProc.GetFileHeader()
    fileProc.PrintFileDetails()
    print()

        



        
        
