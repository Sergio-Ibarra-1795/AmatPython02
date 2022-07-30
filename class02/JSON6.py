#Ejercicio 6 de JSON
#Descripción: Obtener peliculas más recientes utilizando la API de https://api.themoviedb.org/
import urllib.request 
import json 

from api_key import * 

## Esta es la URL que necesitamos para usar la API de THE Movie
url1_1 = (f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3fd2be6f0c70a2a598f084ddfb75487c&page=1')

with urllib.request.urlopen(url1_1) as respuesta: ##Para abrir la URL del API
    response = respuesta.read() ##ESTE ya tiene el archivo en formato JSON
    movies = json.loads(response) ##Tiene un diciconario con la información de las noticias

    for value in movies['results']:
        try:
            print("*******************************************************")
            print(f"{value['original_title']}")
            print(f"{value['overview']}")
            print(f"https://image.tmdb.org/t/p/w1280/{value['poster_path']}")
        except:
            pass





