# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:30:00 2018

@author: Leonardo-PC
"""
import sys
import json




def Concordancia(doc, find_term):
    coincidences = 0
    for palabra in doc:
        if palabra == find_term:
            coincidences+= 1
    return coincidences
    
def main(args): 
    
    # VARIABLES 
    # -----------------------
    palabras = noticias = ""
    # -----------------------
    # Obtenemos el diccionario 
    Json_palabra = []
    palabras  = open(r'Doc\palabras.txt', "r")
    Json_palabra = json.JSONDecoder().decode(palabras.read())
    # -----------------------
    # Obtenemos el documento
    Json_noticia = []
    noticias  = open(r'Doc\noticias.txt', "r")
    Json_noticia = json.JSONDecoder().decode(noticias.read())
    # -----------------------

    listword = {}
    for contador, doc in Json_noticia.items():
        x = []
        for palabra in Json_palabra:
            x.append(Concordancia(doc, palabra))
        # Concordancias por cada noticia    
        listword[contador] = x

    file = open(r"Doc\VectorSpace.txt", "w")
    file.write(json.JSONEncoder().encode(listword))
    file.close()    
  

# metodo main
if __name__ == '__main__':
    main(sys.argv)

