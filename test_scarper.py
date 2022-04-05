import requests
import bs4


result = requests.get('https://www.proxyhub.me/en/au-socks5-proxy-list.html')
soup = bs4.BeautifulSoup(result.text, 'lxml')



def get_line(n):
    ip = soup.select('td')[n].getText()
    port = soup.select('td')[n+1].getText()
    print(ip)
    print(port)
    f = open('ip.txt', 'a')
    f.write(ip + ' ' + port + '\n')
    f.close()


n = 0

while n < 115:
    get_line(n)
    n = n + 6