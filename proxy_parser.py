import requests
from bs4 import BeautifulSoup


#result = requests.get('https://hidemy.name/ru/proxy-list/')


#soup = bs4.BeautifulSoup('soup.tr', 'html.parser')
with open("https://hidemy.name/ru/proxy-list/") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')