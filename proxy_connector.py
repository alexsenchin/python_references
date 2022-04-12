import requests


proxies = {
    'https': 'https://109.72.231.37:1080'
}






def get_connection():
    print('[+] Trying to set a connection')
    data = requests.get('https://ipinfo.io/json', proxies=proxies, timeout=30000)
    print(data.text)

get_connection()
