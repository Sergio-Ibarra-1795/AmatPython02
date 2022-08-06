# Ejercicio 6 de scraping
# Autor: Goz
# Descripción: Obtener información de las imágenes de una página utilizando bs4
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://gozdeveloper.com/demo2')
bs = BeautifulSoup(html.read(), 'html.parser')

images = bs.find_all('img', {'src':re.compile('[A-Za-z]*.[png|jpg]')})
for image in images:
   print('https://gozdeveloper.com/demo2/' + image['src'])
