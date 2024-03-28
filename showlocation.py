# Parses the json output from termux-location command
# and prints certain fields in more human readable form

# Termux json fields:
# latitude, longitude, altitude, accuracy, vertical accuracy, bearing
# speed, elapsedMs, provider
# All of the above are numerical fields except for provider (usually "gps")

import json
import subprocess
import math

# Function to convert lat/long to degree, minutes, seconds text
# This function assumes latlongfloat is positive
def toDMStext(latlongfloat):
    degint = math.floor(latlongfloat) # this is type int
    minutes = 60*(latlongfloat - float(degint))
    minutesint = math.floor(minutes) # this is type int
    seconds = 60*(minutes - float(minutesint)) # this is type float
    DMStext = "%d" % degint
    DMStext += chr(176) + " "
    DMStext += ("%d" % minutesint) + "' "
    DMStext += "%.1f" % seconds + '"'
    return DMStext

# Function to convert speed to km/h
def tokmh(speedmetrespersec):
    return (60*60*speedmetrespersec)/1000
    
# Function to output bearing as a compass direction text, e.g. ENE, NE etc
def tocompasspt(bearing):
    compasspttxt = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    x = round(bearing/22.5)  # this should be an int
    if (x == 16):
        x = 0
    return compasspttxt[x]


# To catch exceptions here in case command fails
try:
    getoutput = subprocess.Popen("termux-location", shell=True, stdout=subprocess.PIPE).stdout
    # For testing using sample output
    # getoutput = subprocess.Popen("cat sampleoutput.txt", shell=True, stdout=subprocess.PIPE).stdout
    output = getoutput.read()
    d = json.loads(output)
except:
    exit("Error 1!")

if not(isinstance(d, dict)) or not(d):
    exit("Error 2!")

# return type is <class 'float'>
# print(type(d["latitude"]))
# print(d["latitude"])

if (d["latitude"] >= 0):
    print("Latitude: " + toDMStext(d["latitude"]) + " N")
else:
    print("Latitude: " + toDMStext(-1.0 * d["latitude"]) + " S")

if (d["longitude"] >= 0):
    print("Longitude: " + toDMStext(d["longitude"]) + " E")
else:
    print("Longitude: " + toDMStext(-1.0 * d["longitude"]) + " W")

print("Altitude: " + "%.2f" % d["altitude"] + " m")

print("Speed: " + "%.2f" % d["speed"] + " m/s, " + "%.2f" % tokmh(d["speed"]) + " km/h")

print("Bearing: " + "%.2f" % d["bearing"] + chr(176) + " (" + tocompasspt(d["bearing"]) + ")")

