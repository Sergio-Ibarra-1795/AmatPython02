# Ejercicio 5 de scraping
# Autor: Goz
# Descripción: Obtener toda la información de una página utilizando bs4
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/demo2')
bs = BeautifulSoup(html.read(), 'html.parser')

print("Cosechando Nuestra Cerveza")
print("*****************************************")
brew = bs.find('div', id = 'brew')
print(brew.text)

print("Cosechando Cerveza artesanal")
print("*****************************************")
beer = bs.find('div', id = 'beer')
print(beer.text)

print("Cosechando ¿Quiéres comprar?")
print("*****************************************")
buy = bs.find('div', id = 'buy')
print(buy.text)

print("Cosechando Promociones")
print("*****************************************")
deals = bs.find('div', id = 'deals')
print(deals.text)
