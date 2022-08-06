# Ejercicio 3 de scraping
# Autor: Goz
# Descripción: Obtener información de una página utilizando bs4
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/website2/index.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# Sacando información de un div con id
content = bs.find('div', id = 'content')
content = bs.find('div', id = 'content').text
print(content)

# Sacando todas las urls del menu
links = bs.find_all('li')
for link in links:
    print(link.a['href'])