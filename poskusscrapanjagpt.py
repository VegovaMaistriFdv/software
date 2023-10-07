import requests

url = 'https://s3wfa.esa.int/api/csv-export?bounds%5Bnwlat%5D=87.509706297451&bounds%5Bnwlon%5D=-360&bounds%5Bselat%5D=-84.89714695160268&bounds%5Bselon%5D=540.0000000000001&zoom=2&date=2023-07-01&date_end=2023-07-31&indexname=s3fires_solar_zenith&satellite=S3A'
r = requests.get(url, allow_redirects=True)

open('.\esa\dat.cvs', 'wb').write(r.content)