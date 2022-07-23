##Ejercio 3CSV
##Abriendo un CSV separado por pipes y recorriendo linea por linea. 
##Utilizaremos la biblioteca csv 
##Ruta a biblioteca: https://docs.python.org/3/library/csv.html

## Importamos biblioteca csv
import csv 

##Abriendo y recorriendo un csv con whith 
with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class01\videogames2.csv','r',encoding='utf-8', newline='') as csv_file4:
    videogames_csv = csv.reader(csv_file4, delimiter='|')
    print(type(videogames_csv))

    for row in videogames_csv: 
        print(f'{row[0]} de la consola {row[1]} se lanzó en {row[2]} con el personaje {row[3]}')

