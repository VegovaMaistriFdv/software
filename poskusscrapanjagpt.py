import requests
from datetime import date
import urllib
import os

today = date.today()

url = 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=87.509706297451&bounds%5Bnwlon%5D=-360&bounds%5Bselat%5D=-84.89714695160268&bounds%5Bselon%5D=540.0000000000001&zoom=2&date=2023-07-01&date_end=2023-07-31&indexname=s3fires_solar_zenith&satellite=S3A'
r = requests.get(url, allow_redirects=True)

open('.\esa\dat.cvs', 'wb').write(r.content)

file = open('.\esa\dat.cvs', 'r')
line2 = []
line = file.readline()

while True:
    line = file.readline()
    if not line:
        break
    line1 = line[96:115]
    line2.append(line1)
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
    sirina = line[x1:x2]
    dolzina = line[x2+1: ]


    print(line1)
    print(sirina)
    print(dolzina)




file = open('.\esa\dat_obdelano', 'a') # Open a file in append mode
file.close()
