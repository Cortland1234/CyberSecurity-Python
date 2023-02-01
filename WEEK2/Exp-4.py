'''
Copyright (c) 2019 Python Forensics, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

'''
from __future__ import print_function
#
# Experimenting with 
# Python Lists
# Python Fundementals
#
# Python Forensics, Inc.
#
print("\nLab-3 Python Lists\n")

# List Demonstration

print("Simple Demonstration of 1Lists in Python")
print("=======================================")
print()

# Create an empty list
emptyList = []

print("Empty List ", emptyList)
print()

# Create a list with initial values
testList = ['Suspect', 'Witness', 'Victim']
print("Initialized List ",testList)
print()

# Append a value to a list
testList.append("Accomplice")
print("Appended List ",testList)
print()

# Insert a value into the list
testList.insert(2, "Informant")
print("Inserted List ", testList)
print()

# Pop a value off the list
popValue = testList.pop()
print("Value Popped from List ",popValue)
print("New List ", testList)
print()

# Interate through the list
print("Iterate through the list")
for value in testList:
    print(value)

print()

# Sorting a list

testList.sort()
print("Sorted List = ", testList)
print()

# A more complex List

complexList = ["John Doe", ["Age", 50], ["Height", 5, 6]]
for eachItem in complexList:
    print(eachItem)

for eachItem in complexList:
    if type(eachItem) == list:
        for eachValue in eachItem:
            print(eachValue, end=" ")
        print
    else:
        print(eachItem)
