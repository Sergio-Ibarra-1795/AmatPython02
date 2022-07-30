#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/              

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re

html = urlopen('https://gozdeveloper.com/demo2/index.html')
bs = BeautifulSoup(html.read(), 'html.parser')

images = bs.find_all('img', {'src':re.compile('[A-Za-z]*.[png|jpg]')})
for image in images:
   print(image['src'])
   url = f"https://gozdeveloper.com/demo2/{image['src']}"
   urllib.request.urlretrieve(url, R"C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\Amat_python02\class02_1\WebScrap5.py\{image['src']}")

gallery_images = bs.find_all('a', {'href':re.compile('img\/[A-Za-z]*.[png|jpg]')})
for gallery_image in gallery_images:
   print(gallery_image['href'])

