#!/usr/bin/envpython

import requests
import bs4
import json


zip = input('Enter ZIP code >>> ')




def socks5_proxyhub(n):
    result_proxyhub = requests.get('https://www.proxyhub.me/en/au-socks5-proxy-list.html')
    soup = bs4.BeautifulSoup(result_proxyhub.text, 'lxml')
    ip = soup.select('td')[n].getText()
    port = soup.select('td')[n+1].getText()
    request_url = 'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    postal = result['postal']
    if postal == zip:
        print('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal)
        f = open('ip.txt', 'a')
        f.write('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal + '\n')
        f.close()
    else:
        print('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal)


n = 0
"""
while n < 115:
    socks5_proxyhub(n)
    n = n + 6
"""
##############################################################################

def soks5_github_list1():
    result = requests.get('https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt')
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    soup.select('.js-file-line')
    for item in soup.select('.js-file-line'):
        data = item.text.split(':')
        ip = data[0]
        port = data[1]

        request_url = 'https://geolocation-db.com/jsonp/' + ip
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        country_code = str(result['country_code'])
        postal = result['postal']
        try:
            if country_code == 'AU' and zip == postal:
                print('IP: ' + ip + ' | ' + 'PORT: ' + port + ' | ' + 'ZIP: ' + postal)
                f = open('ip.txt', 'a')
                f.write('IP: ' + ip + " | " + "PORT: " + port + " | " + "ZIP: " + postal + '\n')
                f.close()
            else:
                print('IP: ' + ip + ' | ' + 'PORT: ' + port + ' | ' + 'ZIP: ' + postal)
        
        except:
                print('No data')


try:
    soks5_github_list1()
except:
    print('List check finished!')
    