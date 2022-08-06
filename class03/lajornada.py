# Ejercicio de Web Scraping
# Autor: Goz
# Descripción: Cosechar información de una página web para uso personal (lectura posterior, análisis)
#              Utilizaremos las bibliotecas os, time, pyfiglet, clint, bs4, requests
#

from my_functions import *
from my_configuration import *

clear()
status = True

while status:
    show_header()
    show_options()
    selection = input('¿Qué quieres hacer? ')
    status2 = True

    if selection == '1':
        while status2:
            status2 = print_notices(politics_web, 'politica')    
    elif selection == '2':
        while status2:
            status2 = print_notices(economy_web, 'economia')
    elif selection == '3':
        while status2:
            status2 = print_notices(world_web, 'mundo')
    elif selection == '4':
        while status2:
            status2 = print_notices(states_web, 'estados')  
    elif selection == '5':
        while status2:
            status2 = print_notices(capital_web, 'capital')  
    elif selection == '6':
        while status2:
            status2 = print_notices(society_web, 'sociedad')  
    elif selection == '7':
        while status2:
            status2 = print_notices(science_web, 'ciencia-y-tecnologia')  
    elif selection == '8':
        while status2:
            status2 = print_notices(culture_web, 'cultura')  
    elif selection == '9':
        while status2:
            status2 = print_notices(sports_web, 'deportes')
    elif selection == 'a':
        while status2:
            status2 = scrap_notices(all_notices)
    elif selection == 'b':
        while status2:
            status2 = scrap_notices_complete(all_notices)
    elif selection == 's':
        status = False
        clear()
    else:
        pass

