#Ejercicio 4 de JSON
#Descripción: Lectura de un archivo JSON CON MUCHOS DATOS 
import json 

counter = 0 

with open(R'C:\Users\Sergio\Documents\SIR_Personal_Dell\Other_courses\PythonAmatDell\magic.json',encoding='utf-8') as json_file:
    data = json.load(json_file)

    for key, value in data.items():
        for card in value:
            print("***************************")
            print(card['name'])
            print(card['released_at'])
            print(card['rarity'])
            if len(card['keywords']) > 0:
                print(','.join(card['keywords']))
            if "image_uris" in card:
                print(card['image_uris']['normal'])
            if "power" in card:
                print(card['power'])
            if "toughness" in card:
                print(card['toughness'])
            print(card['scryfall_set_uri'])
            counter += 1

print(counter)


            
