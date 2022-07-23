## Importamos biblioteca csv
import csv 

##Abriendo un CSV con open()
my_csv1_1 = open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\olympics2.csv','r',encoding='utf-8')
olympics_csv = csv.reader(my_csv1_1)
print(olympics_csv)


##Creando una lista de listas 
olympics_list2 = list(olympics_csv)
#print(olympics_list)

for medal in olympics_list2: 
    year=medal[0]
    city=medal[1]
    sport= medal[2]
    discipline = medal[3]
    athlete = medal[4]
    country = medal[5]
    gender = medal[6]
    event= medal[7]
    place = medal[8]

    if country == "USA":
        print(f"{city} {year} - {athlete} - {sport} {discipline} {event} {place}")



