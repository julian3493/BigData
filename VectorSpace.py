# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:30:00 2018

@author: Leonardo-PC
"""
import sys
import json
from time import time

# Metodo que retorna la frecuencia de cada palabra en una notica 
def CalcularFrecuencia(doc, v_palabra):
    coincidences = 0
    for palabra in doc:
        if palabra == v_palabra:
            coincidences = coincidences +  1
    return coincidences
    
def main(args): 
    
    # VARIABLES 
    # -----------------------
    palabras = noticias = ""
    tiempoInicial = time()
    # -----------------------
    # Obtenemos el diccionario palabras.txt 
    Json_palabra = []
    palabras  = open(r'Doc\palabras.txt', "r")
    Json_palabra = json.JSONDecoder().decode(palabras.read())
    # -----------------------
    # Obtenemos el documento noticas.txt
    Json_noticia = []
    noticias  = open(r'Doc\noticias.txt', "r")
    Json_noticia = json.JSONDecoder().decode(noticias.read())
    # -----------------------

    vectorSpace = {}
    for id, noticia in Json_noticia.items():
        vectorSpaceItems = []
         # Concordancias de cada palabra en la notica  (solo en una noticia)   
        for palabra in Json_palabra:
            vectorSpaceItems.append(CalcularFrecuencia(noticia, palabra))
       
        #Se almacena el nuevo vector con la frecuencia de cada palabra en una noticia.
        vectorSpace[id] = vectorSpaceItems

    #Se crea documento .txt donde se guarda resultado de la operacion. 
    file = open(r"Doc\VectorSpace.txt", "w")
    file.write(json.JSONEncoder().encode(vectorSpace))
    file.close()  
    
    #Calculamos e imprimimos el tiempo en realizar la operacion...
    tiempoFinal = (time() - tiempoInicial)
    print("Hecho en...", tiempoFinal)
  

# metodo main
if __name__ == '__main__':
    main(sys.argv)

