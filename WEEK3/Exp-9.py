'''
Simple Class Example
'''
from __future__ import print_function
import sys

class systemInfo:
    ''' Simple SystemInfo Class that obtains
        the major python version and the 
        operating system type
    '''
    def __init__(self):
        ''' Create object variables and Constants '''
        if sys.version_info[0] < 3:
            self.PYTHON_VERSION = 2
        else:
            self.PYTHON_VERSION = 3
        
        self.OS = sys.platform
        
    def PrintSysInfo(self):
        ''' Print out the system information '''
        print(self.PYTHON_VERSION)
        print(self.OS)
        
sysInfo = systemInfo()              # create an object

print(sysInfo.PYTHON_VERSION)       # print the PYTHON_VERSION
print(sysInfo.OS)                   # print the OS

# Invoke the object PrintSysInfo Method
sysInfo.PrintSysInfo()




