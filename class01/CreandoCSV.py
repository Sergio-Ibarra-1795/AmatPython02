##Ejercio 5CSV
##Creando csv desde cero   
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

## Creamos un archivo csv desde cero en PYTHON y agregamos filas

created_csv = open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\videogames1_1.csv','w',encoding='utf-8',newline='') 
created_videogames_csv = csv.writer(created_csv)
created_videogames_csv.writerow(['DonkeyKong','snes','1994','kong'])
created_videogames_csv.writerow(['DonkeyKong2','snes','1996','kong'])
created_videogames_csv.writerow(['DonkeyKong3','snes','1998','kong'])
created_csv.close()
