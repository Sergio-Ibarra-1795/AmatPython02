#Ejercio 6CSV
##Crear un CSV con información de diccionarios   
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Creando un csv con información de diccionario 
with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\games3.csv', 'w',newline='', encoding='utf-8') as csv_file:
    columnas_header = ['videogame','console','year','main_character']
    writer=csv.DictWriter(csv_file,fieldnames=columnas_header) ##Para crear el archivo tipo diccionario 
    writer.writeheader()##PARA QUE ESCRIBA LA CABECERA EN EL ARCHIVO
    writer.writerow({'videogame':'call of duty1', 'console':'ps4','year':2011, 'main_character':'soldier'})
    writer.writerow({'videogame':'call of duty2', 'console':'ps4','year':2013, 'main_character':'soldier'})
    writer.writerow({'videogame':'call of duty3', 'console':'ps4','year':2015, 'main_character':'soldier'})
    writer.writerow({'year':2015,'console':'ps4', 'main_character':'soldier','videogame':'test'})



