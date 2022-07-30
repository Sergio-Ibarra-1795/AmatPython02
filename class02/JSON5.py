#Ejercicio 5 de JSON
#Descripción: Obtener noticias mundiales en la API de https://newsapi.org/
import urllib.request 
import json 

from api_key import * 

## Esta es la URL que necesitamos para usar la API de NEWsAPI
url1 = (f'https://newsapi.org/v2/top-headlines?country=mx&{key}')

with urllib.request.urlopen(url1) as respuesta: ##Para abrir la URL del API
    response = respuesta.read() ##ESTE ya tiene el archivo en formato JSON
    news = json.loads(response) ##Tiene un diciconario con la información de las noticias

    print(f"Se encontraron: {news['totalResults']}")

    for i in range(news['totalResults']):
        try:
            print(f"{news['articles'][i]['title']}")
            print(f"{news['articles'][i]['author']}")
            print(f"{news['articles'][i]['description']}")
            print(f"{news['articles'][i]['content']}")
            print(f"{news['articles'][i]['url']}")
            print('**********************************')
        except:
            pass


