import requests
import bs4


result = requests.get('https://cs.money/ru/csgo/store/')
soup = bs4.BeautifulSoup(result.text, 'lxml')


soup.select('CardCsgo_name__3DeMh')
for item in soup.select('CardCsgo_name__3DeMh'):
    print(item.text)