##Ejercio 3CSV
##Abriendo un CSV con with y recorriendo linea por linea el arcihvo. 
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Abriendo y recorriendo un csv con whith 
with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\olympics.csv','r',encoding='utf-8', newline='') as csv_file3:
    olympics_csv = csv.reader(csv_file3)
    print(type(olympics_csv))

    for row in olympics_csv: 
        print(row)
