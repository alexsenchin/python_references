import requests


proxies = {
    'https': 'https://195.2.71.201:16072'
}



data = requests.get('https://ipinfo.io/json', proxies=proxies)
print(data.text)


