##Ejercicio 1 de JSON
##Descripción:Obtener información de un archiv JSON
    ##Utilizaremos la biblioteca JSON que está dentro de las baterias incluidas de PYTHON

##Importamos la biblioteca JSON
import json 

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\countries.json' ,encoding='utf-8') as json_file:
    data_set_countries= json.load(json_file) ##Para CARGAR el archivo como Diccionario (estilo JSON) en Python 
    for country in data_set_countries:
        print(f"País: {country['name']}")
        print(f"Capital: {country['capital']}")
        print(f"Descripción: {country['description']}")

print(type(data_set_countries))
