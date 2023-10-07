import requests
import datetime 
import pandas as pd


today = datetime.date.today()
today = pd.to_datetime(datetime.date.today(), format="%Y-%m-%d") - pd.DateOffset(days=3)
today = str(today)
today =today[0:10]
today = str(today)
print(today)



today_30 = pd.to_datetime(datetime.date.today(), format="%Y-%m-%d") - pd.DateOffset(months=1)
today_30 =str(today_30)
today_30 =today_30[0:10]
today_30 =str(today_30)
print(today_30)




#url= 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=87.509706297451&bounds%5Bnwlon%5D=-360&bounds%5Bselat%5D=-84.89714695160268&bounds%5Bselon%5D=540.0000000000001&zoom=2&date='+today+'&date_end='+today_30+'&indexname=s3fires_solar_zenith&satellite=S3A'
url= 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=81.72318761821157&bounds%5Bnwlon%5D=-247.50000000000003&bounds%5Bselat%5D=-73.22669969306126&bounds%5Bselon%5D=427.50000000000006&zoom=2&date=' + today_30 + '&date_end=' + today + '&indexname=s3fires_solar_zenith&satellite=S3A'
#url= 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=81.72318761821157&bounds%5Bnwlon%5D=-247.50000000000003&bounds%5Bselat%5D=-73.22669969306126&bounds%5Bselon%5D=427.50000000000006&zoom=2&date=2023-09-07&date_end=2023-10-04&indexname=s3fires_solar_zenith&satellite=S3A'

#print(url)
#url = str(url)
r = requests.get(url, allow_redirects=True)
open('.\esa\dat.cvs', 'wb').write(r.content)

file = open('.\esa\dat.cvs', 'r')
time = []
line = file.readline()

width = []
length = []

while True:
    line = file.readline()
    if not line:
        break
    line1 = line[96:115]
    time.append(line1)
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
    width1 = line[x1:x2]
    width.append(width1)
    length1 = line[x2+1:-1]
    length.append(length1)



file = open('.\esa\dat_cas', 'w')
file.write(str(time))
file.close()

file = open('.\esa\dat_sirina', 'w')
file.write(str(width))
file.close()


file = open('.\esa\dat_dolzina', 'w')
file.write(str(length))
file.close()