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


get_line(0)
get_line(6)
get_line(12)
get_line(18)
get_line(24)
get_line(30)
get_line(36)
get_line(42)
get_line(48)
get_line(54)
get_line(60)
get_line(66)
get_line(72)
get_line(78)
get_line(84)
get_line(90)
get_line(96)
get_line(102)
get_line(108)
get_line(114)