import requests
import bs4

result = requests.get('https://www.proxyhub.me/en/au-socks5-proxy-list.html')
type(result)
requests.models.Response
result.text