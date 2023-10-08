import requests
import datetime 
import pandas as pd
import requests
import json
from decouple import config


MAP_KEY = config("MAP_KEY")
SOURCE = config("MAP_SOURCE")
AREA_COORDINATES = config("MAP_AREA")
DAY_RANGE = config("RANGE")
YES_NO = config("DOWNLOWD")

YES_NO = int(YES_NO)

if YES_NO == 1:  
    url= 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/'+MAP_KEY+'/'+SOURCE+'/'+AREA_COORDINATES+'/'+DAY_RANGE
    r = requests.get(url, allow_redirects=True)
    open('./nasa/nasa.cvs', 'wb').write(r.content)

##url= 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + MAP_KEY + '/VIIRS_NOAA20_NRT/world/1'

file = open('./nasa/nasa.cvs', 'r')
line = file.readline()

time_temp = []
latitude_temp = []
longitude_temp = []

while True:
    line = file.readline()
    if not line:
        break
    
    i = 0
    for x in range(len(line)):
        if line[x] == ',':
            i = i + 1  
            if i == 1:
                x1 = x
            if i == 2:
                x2 = x
            if i == 5:
                x3 = x
    latitude_temp_1 = line[0:x1]
    latitude_temp.append(latitude_temp_1)
    longitude_temp_1 = line[x1+1:x2]
    longitude_temp.append(longitude_temp_1)
    time_temp_1 = line[x3+1: x3+11] + "T"
    time_temp.append(time_temp_1)



l = 0
latitude = []
longitude = []
time_of = []

latitude_min = config("LATITUDE_MIN")
latitude_max = config("LATITUDE_MAX")

longitude_min = config("LONGITUDE_MIN")
longitude_max = config("LONGITUDE_MAX")

while l < len(latitude_temp):
    if (latitude_temp[l] <=  str(latitude_max)) and (latitude_temp[l] >= str(latitude_min)) and (longitude_temp[l] <= str(longitude_max)) and (longitude_temp[l] >= str(longitude_min)):
        latitude.append(latitude_temp[l])
        longitude.append(longitude_temp[l])
        time_of.append(time_temp[l])
    l = l +1

#FOR DEBUG 
#file = open('./nasa/nasa_sirina', 'w')
#file.write(str(latitude))
#file.close()
#file = open('./nasa/nasa_dolzina', 'w')
#file.write(str(longitude))
#file.close()
#file = open('./nasa/nasa_cajt', 'w')
#file.write(str(time_of))
#file.close()

# uploading to server with jonson

url_1 = config("URL_API")

fires = []
for y in range(len(latitude)):
    fires.append({"timestamp":time_of[y] ,"latitude": latitude[y]  ,"longitude":longitude[y]})

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url_1, data=json.dumps({"fire":fires}), headers=headers)

print(r)