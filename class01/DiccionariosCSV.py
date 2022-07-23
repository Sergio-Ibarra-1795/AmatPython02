##Ejercio 6CSV
##Diccionarios con CSV  
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Ejemplo de diccionario
grocery_list = {
    'cheese':'manchego',
    'fruit':['apple','orange'],
    'toys':'BZL'
}


##Abriendo un csv para crear una lista de dicionarios 

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\videogames1.csv','r',encoding='utf-8',newline='') as csv_file:
    my_csv_dic = csv.DictReader(csv_file) ##SE INDICA QUE LEA EL ARCHIVO COMO UN DICICONARIO 
    videogames =[] ##Nostros inicializamos esto como una lista
    for row in my_csv_dic:
        videogames.append(dict(row))
        print(dict(row))
        print(type(dict(row)))

print(videogames)
print(type(videogames))

