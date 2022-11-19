"""
construirás una Pokédex obteniendo los datos de https://pokeapi.co/

Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le mande un mensaje de error; si existe, que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 

Posteriormente, guardarás toda la información del pokémon (junto con el link de la imagen frontal del pokémon) en un archivo .json dentro de una carpeta llamada “pokedex”.

Habiendo hecho esto, subirás el código a un repositorio en tu cuenta de GitHub explicando cómo lo hiciste, qué bibliotecas necesitaría otro usuario para ejecutar el proyecto, mostrando imágenes de muestra de algún resultado de búsqueda de un pokémon y describiendo qué has aprendido en este módulo.


"""
import requests
import matplotlib.pyplot as plt
import json                           #se importan las librerias necesarias
from PIL import Image
from urllib.request import urlopen
import os
print("******POKEDEX******")

pokemon=input("dime el nombre del Pokemón : ")

url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"     #le pedimos al usuario el nombre del pokemon para poder y  llamamos  la Api en interactuar con la url
                                                      
respuesta=requests.get(url)
while True:
    if respuesta.status_code!=200:
        print("Pokemon no encontrado, vuelva a inicia programa")  #condicionamos que no haya error de estatus mediante un cilo while.
        exit()
    else:
        

        datos=respuesta.json()       
        nombre=datos["name"]  
        tamaño=datos["height"]                  #rescatamos la valores mediante variables indicando su ubicacion en la libreria de la api
        peso=datos["weight"]
        habilidades=datos["abilities"][0]["ability"]["name"]
        tipo=datos["types"][0]["type"]["name"]
        imagen=datos["sprites"]["front_default"]
        total_movimientos=len(datos["moves"])

        try:
            
            os.makedirs('C:\\pokedex_')#creamos  directorio co la funcio makedirs  
            
            
        
        except FileExistsError:
            
            # evitamos el error de que ya existe el  archivo y  manipulamos    
        
            with open("C:\\pokedex_\\pokemon.json","w") as f_archivo_pokemon:
                json.dump(datos,f_archivo_pokemon)                           #abrimos y ceamos  archivo "_archivo_pokemon"  en modo escritura para ingresar datos Y  leemos
                                                                            # y cargamos en el "_archivo_pokemon"  la informacion en formato jason 
            with open ("C:\\pokedex_\\pokemon.json","r") as f_archivo_pokemon:
                json.load(f_archivo_pokemon)
            

        imagen=Image.open (urlopen(imagen))  
        plt.title(datos["name"].capitalize())   #abrimon la imagen ,colocamos el titulo y la mostramos
        imgplot =  plt.imshow(imagen)
        plt.show()

        print(f"Pokemon:    {pokemon}")
        print(f"tipo        {tipo}")
        print(f"Peso :      {peso} lbs")                #imprimimos los datos del pokemon y para los movimientos hacemosmun cilo while para mostrarlos todos
        print(f"tamaño:     {tamaño} cm ")
        print(f"habilidades {habilidades}")
        print("Movimientos: ")
        for i in range(total_movimientos):
            mov=datos["moves"][i]["move"]["name"]
            print(f"\t{mov}" )
        break




