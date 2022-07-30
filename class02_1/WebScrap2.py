#Ejercicio 8 (Webscraping)
#Descripción: Obtener código de una página web Y presentarlo bonito

##Importamos la bibblioteca urllib
from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/website1') ##Para abrir la URL del sitio web deseado
bs = BeautifulSoup(html.read(),'html.parser') ##Genera un archivo tipo sopa que será más fácil de leer bonito 
print(bs.prettify()) ##Lee bonito el resultado del webscrapping
print('Listo')
