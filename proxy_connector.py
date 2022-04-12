import requests
import http.client

proxies = {'https':'https://118.127.102.149:12776'}
r = requests.get('http://grizzlykr.com.ua/', proxies = proxies)
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
result = conn.getresponse().read()
print(result)
print(r.status_code, r.reason)





