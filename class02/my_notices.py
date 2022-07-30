# Importamos la biblioteca requests
import urllib.request
import json
from my_website import *

# Creamos una función que obtenga las noticias y construya la página del sitio
def get_notices(url, myfile, title):

    with urllib.request.urlopen(url) as f:
        response = f.read()
        notices = json.loads(response)   
        html_title = f"""<div style="width:100%; text-align:center; font-size:26px; padding:20px;">{title}</div>"""

        with open(myfile, 'w') as file:
            file.write(html_header)
            file.write(html_body1)
            file.write(html_title)
            
            total = len(notices['articles'])

            for article in notices['articles']:
                fullstring = article['urlToImage']            
      
                notice = f"""
                      <div style="float:left; padding:22px; padding-bottom:0px;">
                      <table style="padding-bottom:0px;">
                        <tr>
                          <td style="padding:22px; text-align:center;" valign="top">
                            <a href="{article['url']}" target="_blank"><img src="{fullstring}" width="220px"></a><br>
                          </td>
                          <td style="padding:22px;">
                            <a href="{article['url']}" style="color:#555; font-weight:bold; font-size:22px;" target="_blank">{article['title']}</a><br>
                            Author: <strong>{article['author']}</strong><br>
                            Published at: <strong>{article['publishedAt']}</strong>
                            <p style="margin-top:8px;"><span>{article['description']}</span></p>
                          </td>
                        </tr>
                        </table>  
                    </div>"""
                file.write(notice)
            file.write(html_body2)

