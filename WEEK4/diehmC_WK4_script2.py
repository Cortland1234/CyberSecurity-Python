'''
EXIF Data Acquistion Example

Name: Cortland Diehm
Date: September 18, 2022
Professor: Alharthi
'''

'''
Using this script provide as a baseline.
Expand the script as follows:

1) Allow the user to enter a path to a directory containing jpeg files.
2) Using that path, process all the .jpg files contained in that folder  (use the testimages.zip set of images)
3) Extract the GPS Coordinates for each jpg (if they exist) and then map the coordinates

NOTE: There are several ways to do this, however, the easiest method would be to use the MapMaker App, at https;//mapmakerapp.com/
      you can either manually enter the lat/lon values your script generates or you can place your results in a CSV file and upload
      the data to the map.

'''
# Usage Example:
# python Assignment 6
#
# Requirement: Python 3.x
#
# Requirement: 3rd Party Library that is utilized is: PILLOW
#                   pip install PILLOW  from the command line
#                   this is already installed in the Virtual Desktop
#==================================================================================================


''' LIBRARY IMPORT SECTION '''
import os                       # Python Standard Library : Operating System Methods
import sys                      # Python Standard Library : System Methods
from datetime import datetime   # Python Standard Libary datetime method from Standard Library

# import the Python Image Library 
# along with TAGS and GPS related TAGS
# Note you must install the PILLOW Module
# pip install PILLOW

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# import the prettytable library
from prettytable import PrettyTable

''' Determine Python Version '''
if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False

def ExtractGPSDictionary(fileName):
    ''' Function to Extract GPS Dictionary '''
    try:
        pilImage = Image.open(fileName)
        exifData = pilImage._getexif()

    except Exception:
        # If exception occurs from PIL processing
        # Report the 
        return None, None

    # Interate through the exifData
    # Searching for GPS Tags

    imageTimeStamp = "NA"
    cameraModel = "NA"
    cameraMake = "NA"
    gpsData = False

    gpsDictionary = {}

    if exifData:

        for tag, theValue in exifData.items():

            # obtain the tag
            tagValue = TAGS.get(tag, tag)
            #print(tagValue)
            # Collect basic image data if available

            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = exifData.get(tag).strip()

            if tagValue == "Make":
                cameraMake = exifData.get(tag).strip()

            if tagValue == 'Model':
                cameraModel = exifData.get(tag).strip()

            # check the tag for GPS
            if tagValue == "GPSInfo":

                gpsData = True;

                # Found it !
                # Now create a Dictionary to hold the GPS Data

                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]

        basicExifData = [imageTimeStamp, cameraMake, cameraModel]    

        '''
        for key, value in gpsDictionary.items():
            print(key, value)
        '''
        
        return gpsDictionary, basicExifData

    else:
        return None, None

# End ExtractGPSDictionary ============================


def ExtractLatLon(gps):
    ''' Function to Extract Lattitude and Longitude Values '''

    # to perform the calcuation we need at least
    # lat, lon, latRef and lonRef
    
    try:
        latitude     = gps["GPSLatitude"]
        latitudeRef  = gps["GPSLatitudeRef"]
        longitude    = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]

        lat, lon = ConvertToDegreesV1(latitude, latitudeRef, longitude, longitudeRef)

        gpsCoor = {"Lat": lat, "LatRef":latitudeRef, "Lon": lon, "LonRef": longitudeRef}

        return gpsCoor

    except Exception as err:
        return None

# End Extract Lat Lon ==============================================


def ConvertToDegreesV1(lat, latRef, lon, lonRef):
    
    degrees = lat[0]
    minutes = lat[1]
    seconds = lat[2]
    latDecimal = float ( (degrees +(minutes/60) + (seconds)/(60*60) ) )
    
    
    if latRef == 'S':
        latDecimal = latDecimal*-1.0
        
    degrees = lon[0]
    minutes = lon[1]
    seconds = lon[2]
    lonDecimal = float ( (degrees +(minutes/60) + (seconds)/(60*60) ) )
    
    if lonRef == 'W':
        lonDecimal = lonDecimal*-1.0
    
    return(latDecimal, lonDecimal)


''' MAIN PROGRAM ENTRY SECTION '''

if __name__ == "__main__":
    '''
    pyExif Main Entry Point
    '''
    print("\nExtract EXIF Data from JPEG Files")

    print("Script Started", str(datetime.now()))
    print()

    ''' PROCESS EACH JPEG FILE SECTION '''
    userInput = input("Enter a directory to scan: ")
    latLonList = []
    
    if os.path.isdir(userInput):
        dirs = os.listdir(userInput)

        ''' Result Table Heading'''
        resultTable = PrettyTable(['File-Name', 'Latitude','Longitude', 'TimeStamp', 'Make', 'Model'])
        
        for eachFile in dirs:
            ''' Set file path '''
            file = os.path.join(userInput, eachFile)
            fileName = os.path.basename(file)
            absPath = os.path.abspath(file)
            ext = os.path.splitext(absPath)[1]  

            targetFile = absPath                
            
            try:            
                if os.path.isfile(targetFile):
                    gpsDictionary, exifList = ExtractGPSDictionary(targetFile)
                                
                    if exifList:
                        TS = exifList[0]
                        MAKE = exifList[1]
                        MODEL = exifList[2]
                    else:
                        TS = 'NA'
                        MAKE = 'NA'
                        MODEL = 'NA'
                    
                        #print("Photo Details")
                        #print("-------------")
                        #print("TimeStamp:    ", TS)
                        #print("Camera Make:  ", MAKE)
                        #print("Camera Model: ", MODEL)
                            
                    if (gpsDictionary != None):
                    
                        # Obtain the Lat Lon values from the gpsDictionary
                        # Converted to degrees
                        # The return value is a dictionary key value pairs
                    
                        dCoor = ExtractLatLon(gpsDictionary)
                        print(dCoor)
                        #print("\nGeo-Location Data")
                        #print("-----------------")
                        
                        if dCoor:
                            lat = dCoor.get("Lat")
                            latRef = dCoor.get("LatRef")
                            lon = dCoor.get("Lon")
                            lonRef = dCoor.get("LonRef")
                                    
                            if ( lat and lon and latRef and lonRef):  
                                #print("Latitude: ", '{:4.4f}'.format(lat))
                                #print("Longitude: ", '{:4.4f}'.format(lon)) 
                                resultTable.add_row([fileName, lat, lon, TS, MAKE, MODEL])
                            else:
                                    print("No GPS EXIF Data")
                        else:
                            print("No GPS EXIF Data")                    
                    else:
                        print(f"Invalid file: {targetFile}")
                    
 
            except:
                print()
        else:
            print()

    # Create Result Table Display using PrettyTable
    ''' GENERATE RESULTS TABLE SECTION'''
    print("EXIF Data Table:")   
    print(resultTable)