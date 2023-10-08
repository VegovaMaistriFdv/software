import requests
import datetime 
import pandas as pd
import requests
import json
from decouple import config


end = config("END")
start = config("START")

end = int(end)
start = int(start)


today = datetime.date.today()
today = pd.to_datetime(datetime.date.today(), format="%Y-%m-%d") - pd.DateOffset(days=end)
today = str(today)
today =today[0:10]

today_30 = pd.to_datetime(datetime.date.today(), format="%Y-%m-%d") - pd.DateOffset(days=start)
today_30 =str(today_30)
today_30 =today_30[0:10]

url= 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=81.72318761821157&bounds%5Bnwlon%5D=-247.50000000000003&bounds%5Bselat%5D=-73.22669969306126&bounds%5Bselon%5D=427.50000000000006&zoom=2&date=' + today_30 + '&date_end=' + today + '&indexname=s3fires_solar_zenith&satellite=S3A'

r = requests.get(url, allow_redirects=True)
open('.\esa\dat.cvs', 'wb').write(r.content)

file = open('.\esa\dat.cvs', 'r')
line = file.readline()

time_temp = []
latetude_temp = []
longetude_temp = []

while True:
    line = file.readline()
    if not line:
        break
    line1 = line[96:115]
    line1 = line1.replace(" ","T")
    line1 = line1 + "Z"
    time_temp.append(line1)
    i = 0
    x1 = 0
    x2 = 0
    for x in range(len(line)):
        if line[x] == ',':
            i = i + 1  
            if i == 6:
                x1 = x +1
            if i == 7:
                x2 = x
    latetude_temp_1 = line[x1:x2]
    latetude_temp.append(latetude_temp_1)
    longetude_temp_1 = line[x2+1:-1]
    longetude_temp.append(longetude_temp_1)

l = 0
latitude = []
longitude = []
time_of = []

latitude_min = config("LATITUDE_MIN")
latitude_max = config("LATITUDE_MAX")

longitude_min = config("LONGITUDE_MIN")
longitude_max = config("LONGITUDE_MAX")

while l < len(latetude_temp):
    if (latetude_temp[l] <=  str(latitude_max)) and (latetude_temp[l] >= str(latitude_min)) and (longetude_temp[l] <= str(longitude_max)) and (longetude_temp[l] >= str(longitude_min)):
        latitude.append(latetude_temp[l])
        longitude.append(longetude_temp[l])
        time_of.append(time_temp[l])
    l = l +1

# FOR DEBUG
#file = open('.\esa\dat_cas', 'w')
#file.write(str(time_of))
#file.close()
#file = open('.\esa\dat_sirina', 'w')
#file.write(str(latitude))
#file.close()
#file = open('.\esa\dat_dolzina', 'w')
#file.write(str(longitude))
#file.close()

# uploading to server with jonson

url_1 = config("URL_API")

fires = []
for y in range(len(latitude)):
    fires.append({"timestamp":time_of[y] ,"latitude": latitude[y]  ,"longitude":longitude[y]})

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url_1, data=json.dumps({"fire":fires}), headers=headers)

print(r)
