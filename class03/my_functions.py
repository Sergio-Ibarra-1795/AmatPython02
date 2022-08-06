import os
import time

from pyfiglet import Figlet
from clint.textui import colored, puts, indent 
import bs4 as bs
import requests

from my_configuration import *

def show_header():
    """Show header with text"""   
    clear() ##Para limpar la panttalla
    f = Figlet(font='slant')
    puts(colored.yellow(f.renderText(header)))

def show_options():
    """Show option's menu"""
    print('\nBIENVENIDO/A')
    print(separator)
    print('¿Qué noticias te interesan? \n')
    with indent(5):
        puts(colored.yellow(' 1.Política '))
        puts(colored.yellow(' 2.Economía '))
        puts(colored.yellow(' 3.Mundo '))
        puts(colored.yellow(' 4.Estados '))
        puts(colored.yellow(' 5.Capital '))
        puts(colored.yellow(' 6.Sociedad '))
        puts(colored.yellow(' 7.Ciencia '))
        puts(colored.yellow(' 8.Cultura '))
        puts(colored.yellow(' 9.Deportes\n '))
        puts(colored.blue(' a. Descargar todos los encabezados'))
        puts(colored.blue(' b. Descargar todo\n'))
    print(separator)
    print('Para salir selecciona (s)')

def get_notices(url, notice_category):
    """Scrap all news from selected category"""
    sauce = requests.get(url, headers=headers)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')
    cards = soup.find_all('div', {'class':{'card card-' + notice_category + ' card-vertical'}})
    notices = []
    for card in cards:
        notice = {}
        notice['title'] = card.find('h2', {'class':{'title-default'}}).get_text()
        notice['url'] = card.find('a')['href']
        notice['description'] = card.find('div', {'class':{'card-text'}}).get_text()
        notices.append(notice)
    return notices

def get_notice(url):
    """Scrap news content"""
    sauce = requests.get('https://www.jornada.com.mx/' + url, headers=headers)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')
    content = soup.find('div', {'id':{'content_nitf'}})
    return content.get_text()

def show_notices(notices_list):
    """Show news list"""
    num = 1
    for count, notice in enumerate(notices_list):
        print(separator)
        print(count + 1, end="")
        puts(colored.yellow(notice['title']))
        print(notice['description'])
        num += 1
    print(separator)

def show_headlines(notices_list):
    """Show news headlines"""
    clear()
    num = 1
    for notice in notices_list:
        print(separator)
        print(num, end="")
        print(notice['title'], end="")
        print(notice['description'])
        num += 1
    print(separator)
    
def create_notices_txt(notices_list):
    """Create txt file with news headlines"""
    with open(my_path + 'noticias.txt', 'w') as file_object:
            num = 1
            for notice in notices_list:
                file_object.write(f'\n{separator}\n')
                file_object.write(str(num) + notice['title'])
                file_object.write(notice['description'])
                file_object.write(notice['url'])
                num += 1

def create_notice_txt(notices, notice_selection):
    """Create txt file with news content"""
    notice_number = int(notice_selection) - 1
    with open(my_path + 'noticia.txt', 'w') as file_object:
        file_object.write(separator)
        file_object.write(notices[notice_number]['title'])
        file_object.write(separator)
        file_object.write(notices[notice_number]['description'])
        file_object.write(notices[notice_number]['url'])
        file_object.write(f'\n{separator}\n')
        url = notices[notice_number]['url']
        content = get_notice(url)
        file_object.write(content)

def show_notice(notices, notice_selection):
    """Show news title, description and url"""
    clear()
    notice_number = int(notice_selection) - 1
    print(separator)
    print(notices[notice_number]['title'])
    print(separator)
    print(notices[notice_number]['description'])
    print(notices[notice_number]['url'])
    print(f'\n{separator}')

def show_complete_notice(notices, notice_selection):
    """Show news title, description, url and content"""
    clear()
    notice_number = int(notice_selection) - 1
    print(separator)
    print(notices[notice_number]['title'])
    print(separator)
    print(notices[notice_number]['description'])
    print(notices[notice_number]['url'])
    print(f'\n{separator}')
    url = notices[notice_number]['url']
    content = get_notice(url)
    print(content)

def show_options2():
    """Show option's menu for all notices"""
    puts(colored.yellow('1. Leer noticia'))
    puts(colored.yellow('2. Descargar las noticias en txt'))
    puts(colored.yellow('3. Regresar a inicio'))

def show_options3():
    """Show option's menu for notice"""
    puts(colored.yellow('1. Leer la noticia completa'))
    puts(colored.yellow('2. Descargar la noticia en txt'))
    puts(colored.yellow('3. Regresar a inicio'))

def print_notices(notices_page, notice_category):
    """Print all notices from a news category"""
    notice_data = get_notices(notices_page, notice_category)
    show_notices(notice_data)
    show_options2()
    selection2 = input('¿Qué quieres hacer con las noticias? ')
    if selection2 == '1':
        status3 = True
        notice_selection = input('Escribe el numero de la noticia: ')
        show_notice(notice_data, notice_selection)
        while status3:    
            show_options3()
            selection3 = input('\n¿Qué quieres hacer con la noticia? ')            
            if selection3 == '1':
                show_complete_notice(notice_data, notice_selection)
            elif selection3 == '2':
                create_notice_txt(notice_data, notice_selection)
            elif selection3 == '3':
                status3 = False
    elif selection2 == '2':
        create_notices_txt(notice_data)
    elif selection2 == '3':
        pass

def scrap_notices(web_list):
    """Scrap all news headlines from website"""
    for notice_section in web_list:
        notices = get_notices(notice_section['url'], notice_section['notice_category'])
        time.sleep(speed1)
        with open(my_path + 'cosecha.txt', 'a') as file_object:
            for notice in notices:
                file_object.write(f'\n{separator}\n')
                file_object.write(notice['title'])
                file_object.write(notice['description'])
                try:
                    file_object.write(notice['url'])
                except:
                    file_object.write('sin url')                        
                print(f"Cosechando {notice['title']}")

def scrap_notices_complete(web_list):
    """Scrap all news content from website"""
    for notice_section in web_list:
        notices = get_notices(notice_section['url'], notice_section['notice_category'])
        time.sleep(speed1)
        with open(my_path + 'cosecha_completa.txt', 'a') as file_object:
            for notice in notices:
                file_object.write(f'\n{separator}\n')
                file_object.write(notice['title'])
                file_object.write(notice['description'])
                file_object.write(notice['url'])
                url = notice['url']
                time.sleep(speed2)            
                print(f"Cosechando {notice['title']}")
                content = get_notice(url)                
                file_object.write(content)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
