#Ejercicio 3 de JSON
#Descripción: Crear un archivo JSON a partir de un diccionario con un DICIONARIO ANIDADO
import json 

my_websites2= {
    'website':'www.python.org',
    'name':'Python programming',
    'area':'programing',
    'development':['web','servers','games'],
    'year':1993,
    'my_float':242.45,
    'status':True,
    'gender':None,
    'creator':{'name':'Guido', 'age':67, 'job':'developer'}
}

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\websites2.json','w' ,encoding='utf-8') as json_file:
    json.dump(my_websites2, json_file)

##Como extra imprimimos el rsultado en pantalla

json_file2 = json.dumps(my_websites2, sort_keys=True, indent=4)
print(json_file2)



