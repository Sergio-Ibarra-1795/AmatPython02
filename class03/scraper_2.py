# Ejercicio 2 de scraping
# Autor: Goz
# Descripción: Obtener código de una página web y presentarlo bonito
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/website1')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.prettify())

