import requests
import json


ip_address = '185.161.201.12'

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
#Results
country_code = str(result['country_code'])
print('Country code: ' + country_code)
country = str(result['country_name'])
print('Country: ' + country)
state = str(result['state'])
print('State: ' + state)
city = str(result['city'])
print('City: ' + city)
latitude = str(result['latitude'])
print('Latitude: ' + latitude)
longitude = str(result['longitude'])
print('Longitude: ' + longitude)
postal = result['postal']
print('Postal code: ' + postal)
print(result)
