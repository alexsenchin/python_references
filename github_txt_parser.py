import requests
import bs4


result = requests.get('https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt')
soup = bs4.BeautifulSoup(result.text, 'lxml')

soup.select('.js-file-line')
for item in soup.select('.js-file-line'):
    data = item.text.split(':')
    ip = data[0]
    port = data[1]
    
    print('IP: ' + ip + ' | ' + 'PORT: ' + port)
    
    
    
    