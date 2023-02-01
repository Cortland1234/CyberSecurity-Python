
'''
Week Two Assignment 2
'''

import os

uniqueWorms = set()

with open("redhat.txt", 'r') as logFile:
    for eachLine in logFile:
        ''' 
        PROF Help, lets start with something simple
        1) Split each line into individual fields
        2) Check to see if the string "worm" exists in that field
           if yes, then print the worm name
        '''
        fieldList = eachLine.split()
        for eachField in fieldList:
            if 'worm' in eachField.lower():
                print(eachField)

        
    


        
        
