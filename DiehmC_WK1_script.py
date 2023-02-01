'''
Week One Assignment - Simple String Searching 

Cortland Diehm
8/26/2022
Assignment #1
'''

'''
Given excerpt from the hacker manifesto 

Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Convert the string to all lower case
3) Count the number characters in the string
4) Count the number of words in the string
5) Sort the words in alphabetical order
6) Search the excerpt variable given below
   For the following and report how many occurances of each are found
   scandal
   arrested
   er
   good
   tomorrow
7) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK1_script.py
                 alharthiD_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

excerpt = " Another one got caught today, it's all over the papers. Teenager\
            Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering\
            Damn kids.  They're all alike"

''' Your work starts here '''

excerpt.lower()

print(excerpt.lower())

print(len(excerpt))

wordcount = len(excerpt.split())

print(wordcount)

sortwords = excerpt.lower().split()

sortwords.sort()

for word in sortwords:
    print(word)

def WordCounters(words): #This function counts the number of instances for each word (which is the parameter)
    print(words,'appears',{excerpt.lower().count(words)},'times')
    
WordCounters('scandal')

WordCounters('arrested')

WordCounters('er')

WordCounters('good')

WordCounters('tomorrow')
