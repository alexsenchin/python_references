import requests

proxies = {
   'http': 'http://proxy.example.com:8080',
   'https': 'http://secureproxy.example.com:8090',
}

url = 'http://http://grizzlykr.com.ua/'

response = requests.post(url, proxies=proxies)
