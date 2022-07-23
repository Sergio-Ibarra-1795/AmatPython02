##Ejercio 1CSV
##Obtener información de un archivo CSV 
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Abriendo un CSV con open()
my_csv1 = open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\olympics.csv','r',encoding='utf-8')
olympics_csv = csv.reader(my_csv1)
print(type(olympics_csv))
#print(olympics_csv)


##Creando una lista de listas 
olympics_list = list(olympics_csv)
print(type(olympics_list))
#print(olympics_list)

for winerAthletes in olympics_list: 
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
        print(f'{city} {year} - {athlete} - {sport} {discipline} {event} {place}')

my_csv1.close()


