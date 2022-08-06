# Ejercicio 7 de scraping
# Autor: Goz
# Descripción: Conocer cuántas veces aparece una cadena de texto en el sitio
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re

html = urlopen('https://gozdeveloper.com/demo2/index.html')
bs = BeautifulSoup(html.read(), 'html.parser')

images = bs.find_all('img', {'src':re.compile('[A-Za-z]*.[png|jpg]')})
for image in images:
   print(image['src'])
   url = f"https://gozdeveloper.com/demo2/{image['src']}"
   urllib.request.urlretrieve(url, f"/home/goz/Courses/taller_python/scripts_3/{image['src']}")

gallery_images = bs.find_all('a', {'href':re.compile('img\/[A-Za-z]*.[png|jpg]')})
for gallery_image in gallery_images:
   print(gallery_image['href'])
   url = f"https://gozdeveloper.com/demo2/{gallery_image['href']}"
   urllib.request.urlretrieve(url, f"/home/goz/Courses/taller_python/scripts_3/{gallery_image['href']}")
