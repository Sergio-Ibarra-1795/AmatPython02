#Ejercicio 7 (Webscraping)
#Descripción: Obtener código de una página web

##Importamos la bibblioteca urllib
from urllib.request import urlopen 

html = urlopen('https://gozdeveloper.com/website1') ##Para abrir la URL del sitio web deseado
print(html.read())
print('Listo')


