# Ejercicio de Programa de escritorio con Tkinter
# Autor:Serg
# Descripción: Aplicación de escritorio para cosechar información de una página web 
#              para uso personal (lectura posterior, análisis)
#              Utilizaremos las bibliotecas tkinter, bs4, requests
#

from itertools import tee
from tkinter import *
from turtle import width 
from my_functions import * 
from my_configuration import * 

app = Tk()

##FUNCIONES
def exit_app(): ##Para agregar boton de cerrado de ventana
    """Exit the program"""
    app.quit()

def scrape_notices(url, notices_category):
    notices = get_notices (url, notices_category) ##Ya tengo mis noticias en notices (Esta linea hace el scraping)
    notices_area.delete(1.0,END) ##Primero borra el contenido de la caja donde se mostrarán noticias
    results = show_notices(notices) ##La variable results apuntando a las noticias ya scrapeadas y bonitas para mostrarse
    notices_area.insert(END, results)

    ##Add label to GUI 
    search_label = Label(app, text='Escrba el núero de la noticia', font=('bold',14),padx=20, pady=20)
    search_label.place(x=460, y=616, anchor='center')
    
    ##Add input for text in GUI
    notice_number = StringVar()
    number_entry = Entry(app, textvariable=notice_number, font=(14), width=15)
    number_entry.place(x=656, y=616, anchor='center')
    ##Add scrape button in GUI
    search_btn = Button(app, text='COSECHAR', width=12, command= lambda: scrape_notice(notices, number_entry.get()))
    search_btn.place(x=756, y=616, anchor='center')

    ##Add download button to GUI: 
    download_btn = Button(app, text='GENERAR TXT', width=12, command= lambda: create_notice_txt(notices_area.get(1.0,"end-1c")))
    download_btn.place(x=80, y=560, anchor='center')

def create_notice_txt(notice):
    """Save scraped info in txt"""
    with open (my_path + 'noticias.txt','a') as file_object:
        file_object.write(notice)
    name_label['text'] = 'El archivo fue creado'

def scrape_notice(notices, notice_number):
    """Scrape notices"""
    notice = get_notice(notices[int(notice_number)-1]['url'])
    notices_area.delete(1.0, END)
    notices_area.insert(END,notice)

##INTERFAZ GRÁFICA

app.title('Cosechador')
app.geometry('1024x670')


# Title label
name_label = Label(app, text=header, font=('bold', 18), padx=20, pady=20)
name_label.place(x=512, y=36, anchor="center")


# Instructions label
message_label = Label(app, text='Por favor selecciona una categoría para iniciar tu cosecha', font=('bold', 12), padx=11, pady=11)
message_label.place(x=512, y=76, anchor="center")


##News content section 
notices_area = Text(app, height=26, width=97, padx=18, pady=18)
notices_area.place(x=160, y=100)
notices_area.delete(END)


##Menu buttons 
politics_btn = Button(app, text='POLÍTICA', width=12, command= lambda: scrape_notices(politics_web, 'politica'))
politics_btn.place(x=80, y=140, anchor="center")

economy_btn = Button(app, text='ECONOMÍA', width=12, command= lambda: scrape_notices(economy_web, 'economia'))
economy_btn.place(x=80, y=180, anchor="center")

world_btn = Button(app, text='MUNDO', width=12, command= lambda: scrape_notices(world_web, 'mundo'))
world_btn.place(x=80, y=220, anchor="center")

states_btn = Button(app, text='ESTADOS', width=12, command= lambda: scrape_notices(states_web, 'estados'))
states_btn.place(x=80, y=260, anchor="center")

society_btn = Button(app, text='SOCIEDAD', width=12, command= lambda: scrape_notices(society_web, 'sociedad'))
society_btn.place(x=80, y=300, anchor="center")

science_btn = Button(app, text='CIENCIA', width=12, command= lambda: scrape_notices(science_web, 'ciencia-y-tecnologia'))
science_btn.place(x=80, y=340, anchor="center")

culture_btn = Button(app, text='CULTURA', width=12, command= lambda: scrape_notices(culture_web, 'cultura'))
culture_btn.place(x=80, y=380, anchor="center")

sports_btn = Button(app, text='DEPORTES', width=12, command= lambda: scrape_notices(sports_web, 'deportes'))
sports_btn.place(x=80, y=420, anchor="center")



##Exist button 
exit_btn = Button(app, text='SALIR', width=12, command = exit_app)##Cuando le de click que hará el boton -command-
exit_btn.place(x=80, y=400, anchor='center') ##.place para localizar elementos donde uno requiera. El (0,0) está arriba a la izquierda

app.mainloop()##Para que la ventana no se cierre


