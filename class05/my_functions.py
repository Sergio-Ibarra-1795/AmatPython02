from tkinter import*
import bs4 as bs
import requests 

from my_configuration import * 

##Para scrapear las noticias (se obtienen las noticias y se guardan en notices)
def get_notices(url, notice_category):
    """Scrap all news from selected category"""
    sauce = requests.get(url, headers= headers)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')
    cards = soup.find_all('div', {'class':{'ljn-nocontpatr card card-' + notice_category + ' card-vertical'}})
    notices = []
    for card in cards:
        notice = {}
        notice['title'] = card.find('h2', {'class':{'title-default'}}).get_text()
        notice['url'] = card.find('a')['href']
        notice['description'] = card.find('div', {'class':{'card-text'}}).get_text()
        notices.append(notice)
    return notices



##Para obtener el contenido de la nota (previamente guardado en notices)
def get_notice(url):
    sauce = requests.get('https://www.jornada.com.mx/' + url, headers=headers)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')
    content = soup.find('div', {'id':{'content_nitf'}})
    return content.get_text()


##Para mostrar las noticias que se seleccionaron 
def show_notices(notices_list):
    notices = """ """
    for count, notice in enumerate(notices_list):
        notices += 'NOTICIA ' + str(count + 1) + '\n'
        notices += separator + '\n'
        notices += notice['title']
        notices += notice['description'] + '\n'
        notices += '\n' + separator + '\n'
    return notices
