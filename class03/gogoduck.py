# Ejercicio de scraping
# Autor: Goz
# Descripción: Utilizar un sitio web con selenium
#    

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# For headless browser
#chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# For headless browser
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://duckduckgo.com")
search_input = driver.find_element(by=By.XPATH, value="(//input[contains(@class, 'js-search-input')])[1]")
#search_input = driver.find_element_by_xpath("(//input[contains(@class, 'js-search-input')])[1]")
search_input.send_keys("dog")

# Clicks in website
#search_btn = driver.find_element_by_id("search_button_homepage")
#search_btn.click()

# Press Keys in website
search_input.send_keys(Keys.ENTER)

#print(driver.page_source)

links = driver.find_elements(By.XPATH, "//div[@class='nrn-react-div']/article/div/h2/a/span")

for link in links:
    print(link.text)

more_link = driver.find_element(By.XPATH, "//a[@class='result--more__btn btn btn--full']")
more_link.click()
more_link = driver.find_element(By.XPATH, "//a[@class='result--more__btn btn btn--full']")
time.sleep(3)
more_link.click()


time.sleep(15000)

driver.close()

time.sleep(15000)
