#Ejercicio 9 (Webscraping)
#Descripción: Sacando informacio´n de un div con ID

##Importamos la bibblioteca urllib
from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen('https://gozdeveloper.com/website2/index.html') ##Para abrir la URL del sitio web deseado
bs = BeautifulSoup(html.read(),'html.parser') ##Genera un archivo tipo sopa que será más fácil de leer bonito 
content = bs.find('div', id='content') ##Para indicar que solo quiero la sección de ID="content"
content_text = bs.find('div', id='content').text ##Para solo extraer el content y no las etiquetas <div>
print(content_text)


##Sacando todas las url (En este caso en el código html LOS ELEMENTOS li SON las URL)
links = bs.find_all('li') ##Es un listado
for link in links: 
    print(link)


##Sacando todas las url (En este caso en el código html LOS ELEMENTOS li SON las URL)
links2 = bs.find_all('li') ##Es un listado
for link2 in links2: 
    print(link2.a['href'])

