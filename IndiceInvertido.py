# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:35:05 2018

@author: Leonardo-PC
"""
import sys
import json


def main(args):
    diccionario = {}
    diccionarioTxt = open(r'Doc\noticias.txt', "r")
    diccionario = json.JSONDecoder().decode(diccionarioTxt.read())
    
    indiceInvertido = {}
    for llave, valor in diccionario.items():
        for palabra in valor: 
            if indiceInvertido.get(palabra,False):
                if llave not in indiceInvertido[palabra]:
                    indiceInvertido[palabra].append(llave)
            else: 
                indiceInvertido[palabra] = [llave]
    
#    print(indiceInvertido)  Prueba 
                
    file = open(r'Doc\Indice_invertido.txt', "w")
    file.write(json.JSONEncoder().encode(indiceInvertido))
    file.close()
        
if __name__ == '__main__': 
    main(sys.argv)
    