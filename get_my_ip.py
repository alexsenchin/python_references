import requests


data = requests.get('https://ipinfo.io/json')

print(data.text)