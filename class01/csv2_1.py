##Ejercio 2CSV
##Obtener información de un archivo CSV 
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Abriendo un csv con whith 

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\olympics.csv','r',encoding='utf-8', newline='') as csv_file:
    olympics_csv = csv.reader(csv_file)

    ##Creando la lista de listas 
    olympics_list2 = list(olympics_csv)

    for winerAthletes in olympics_list2: 
     year=winerAthletes[0]
     city=winerAthletes[1]
     sport= winerAthletes[2]
     discipline = winerAthletes[3]
     athlete = winerAthletes[4]
     country = winerAthletes[5]
     gender = winerAthletes[6]
     event= winerAthletes[7]
     place = winerAthletes[8]

     if country == "MEX" and place=='Gold':
        mexico_winner_i= city + year + athlete + sport + discipline + event + place
        print(mexico_winner_i)
        
 