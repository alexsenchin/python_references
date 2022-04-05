import requests
import bs4


result = requests.get('https://www.proxyhub.me/en/au-socks5-proxy-list.html')
soup = bs4.BeautifulSoup(result.text, 'lxml')

#Grabing all page
#print(result.text)

#soup.select('td')
#for item in soup.select('td'):
#    print(item.text)



