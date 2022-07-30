# Ejercicio 7 de JSON
# Autor: Goz
# Descripción: Obtener noticias de la api de https://newsapi.org/
#              y crear un Sitio Web con la información.
#              Utilizaremos la biblioteca urllib.requests
#              https://docs.python.org/3/library/urllib.request.html


# Importamos nuestras bibliotecas
from my_notices import *
from my_config import *

get_notices(mx, my_path + "mexico.html", "Noticias en México")
get_notices(us, my_path + "usa.html", "Noticias en Estados Unidos")
get_notices(ca, my_path + "canada.html", "Noticias en Canada")
get_notices(fr, my_path + "france.html", "Noticias en Francia")
get_notices(ru, my_path + "rusia.html", "Noticias en Rusia")
get_notices(jp, my_path + "japan.html", "Noticias en Japón")
get_notices(de, my_path + "germany.html", "Noticias en Alemania")

