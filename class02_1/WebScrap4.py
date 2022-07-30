#Ejercicio 10 (Webscraping)
#Descripción: Obtener toda la información de una página utilizando bs4

##Importamos la bibblioteca urllib
from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/website2/index.html') ##Para abrir la URL del sitio web deseado
bs = BeautifulSoup(html.read(),'html.parser') ##Genera un archivo tipo sopa que será más fácil de leer bonito (Todo el código ya está en un objeto tipo BEATUFULSOUP) 

# Sacando todas las urls del menu
links = bs.find_all('li')
for link in links:
    print(f'Cosechando {link.text}')
    print('https://gozdeveloper.com/website2/' + link.a['href'])
    print("*************************************************************")

    html = urlopen('https://gozdeveloper.com/website2/' + link.a['href'])
    print(type(html))
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(type(bs))

    # Sacando información de un div con id
    content = bs.find('div', id = 'content')
    print(content)
    print(type(content))
