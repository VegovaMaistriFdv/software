import requests
from datetime import date


today = date.today()
print(today)

url = 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=87.509706297451&bounds%5Bnwlon%5D=-360&bounds%5Bselat%5D=-84.89714695160268&bounds%5Bselon%5D=540.0000000000001&zoom=2&date=%sdate_end=2023-07-31&indexname=s3fires_solar_zenith&satellite=S3A' ,(today)
r = requests.get(url, allow_redirects=True)

open('.\esa\dat.cvs', 'wb').write(r.content)

file = open('.\esa\dat.cvs', 'r')
cas = []
line = file.readline()

sirina1 = []
dolzina1 = []

while True:
    line = file.readline()
    if not line:
        break
    line1 = line[96:115]
    cas.append(line1)
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
    sirina1.append(sirina)
    dolzina = line[x2+1: ]
    dolzina1.append(dolzina)



file = open('.\esa\dat_cas', 'w')
file.write(str(cas))
file.close()

file = open('.\esa\dat_sirina', 'w')
file.write(str(sirina1))
file.close()


file = open('.\esa\dat_dolzina', 'w')
file.write(str(dolzina1))
file.close()

