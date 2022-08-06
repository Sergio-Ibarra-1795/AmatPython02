header = 'La jornada scraping example'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
separator = '*' * 50
my_path = 'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell'


politics_web = "https://www.jornada.com.mx/category/politica.html"
economy_web = "https://www.jornada.com.mx/category/economia.html"
world_web = "https://www.jornada.com.mx/category/mundo.html"
states_web = "https://www.jornada.com.mx/category/estados.html"
capital_web = "https://www.jornada.com.mx/category/capital.html"
society_web = "https://www.jornada.com.mx/category/sociedad.html"
science_web = "https://www.jornada.com.mx/category/ciencia-y-tecnologia.html"
culture_web = "https://www.jornada.com.mx/category/cultura.html"
sports_web = "https://www.jornada.com.mx/category/deportes.html"

all_notices = [{'url':politics_web, 'notice_category':'politica'},  
               {'url':economy_web, 'notice_category':'economia'}, 
               {'url':world_web, 'notice_category':'mundo'}, 
               {'url':states_web, 'notice_category':'estados'}, 
               {'url':capital_web, 'notice_category':'capital'}, 
               {'url':society_web, 'notice_category':'sociedad'}, 
               {'url':science_web, 'notice_category':'ciencia-y-tecnologia'}, 
               {'url':culture_web, 'notice_category':'cultura'}, 
               {'url':sports_web, 'notice_category':'deportes'}]

# Puedes subir los valores pero NO los bajes para NO afectar al sitio web que cosechamos
# Velocidad a la que cambia entre noticia
speed1 = 5
# Veocidad a la que cambia entre secciones de noticias
speed2 = 10