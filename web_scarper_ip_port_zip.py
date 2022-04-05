import requests
import bs4
import json


result = requests.get('https://www.proxyhub.me/en/au-socks5-proxy-list.html')
soup = bs4.BeautifulSoup(result.text, 'lxml')


def get_line(n):
    ip = soup.select('td')[n].getText()
    port = soup.select('td')[n+1].getText()
    request_url = 'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    postal = result['postal']
    print('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal)
    f = open('ip.txt', 'a')
    f.write('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal + '\n')
    f.close()


n = 0

while n < 115:
    get_line(n)
    n = n + 6