# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:35:05 2018

@author: Leonardo-PC
"""
import sys
import json
from time import time

def main(args):
    noticias = {}
    # Lectura del documento noticias.txt
    noticiasTxt = open(r'Doc\noticias.txt', "r")
    noticias = json.JSONDecoder().decode(noticiasTxt.read())
    # Inicializacion de variables     
    tiempoInicial = time()
    indiceInvertido = {}
    
    for id, noticia in noticias.items():
        for palabra in noticia: 
            if indiceInvertido.get(palabra,False):
                if id not in indiceInvertido[palabra]:
                    indiceInvertido[palabra].append(id)
            else: 
                indiceInvertido[palabra] = [id]
    
    
                
    file = open(r'Doc\Indice_invertido.txt', "w")
    file.write(json.JSONEncoder().encode(indiceInvertido))
    file.close()
    tiempoFinal = (time() - tiempoInicial)
    print("Hecho en...", tiempoFinal)
        
if __name__ == '__main__': 
    main(sys.argv)
    