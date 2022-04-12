import http.client



conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
result = conn.getresponse().read()
print(result)