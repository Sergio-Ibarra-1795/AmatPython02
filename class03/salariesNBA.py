# Ejercicio de scraping
# Autor: Goz
# Descripción: Descargar contenido de un sitio web con selenium
#    

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hoopshype.com/salaries/players/")

players_links = driver.find_elements(By.XPATH, '//td[@class="name"]/a')
links = []
all_players = []

for p in range(51):
    links.append(players_links[p].get_attribute('href'))

for link in links:
    driver.get(link)
    player = {}
    try:
        player_fullname = driver.find_element(By.XPATH, '//div[@class="player-fullname"]')
        player['fullname'] = player_fullname.text
    except:
        player['fullname'] = ""
        pass
    try:
        player_team = driver.find_element(By.XPATH, '//div[@class="player-team"]')
        player['team'] = player_team.text
    except:
        player['team'] = ""
        pass

    print(player)

