# Ejercicio 1 de scraping
# Autor: Goz
# Descripción: Obtener código de una página web
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html


#Importamos la biblioteca urllib
from urllib.request import urlopen

html = urlopen('https://gozdeveloper.com/website1')
print(html.read())
print('Listo!')

