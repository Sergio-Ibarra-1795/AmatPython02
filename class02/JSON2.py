#Ejercicio 2 de JSON
#Descripción: Crear un archivo JSON a partir de un diccionario 
import json 

my_websites= {
    'website':'www.python.org',
    'name':'Python programming',
    'area':'programing',
    'development':['web','servers','games'],
    'year':1993,
    'my_float':242.45,
    'status':True,
    'gender':None
}

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\websites.json','w' ,encoding='utf-8') as json_file:
    json.dump(my_websites, json_file)

##Como extra imprimimos el rsultado en pantalla

json_file = json.dumps(my_websites, sort_keys=True, indent=4)
print(json_file)


