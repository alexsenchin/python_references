import random
import requests
import json


def generate_ip():
    ip1 = str(random.randint(0, 255))
    ip2 = str(random.randint(0, 255))
    ip3 = str(random.randint(0, 255))
    ip4 = str(random.randint(0, 255))
    ip = (ip1 + '.' + ip2 + '.' + ip3 + '.' + ip4)
    return ip


ip_address = generate_ip()


#===================================================


request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)



#=====================================================
#country_code = str(result['country_code'])
#print('Country code: ' + country_code)
#postal = result['postal']
#print('Postal code: ' + postal)
print(result)