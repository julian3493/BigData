# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:48:35 2018

@author: Leonardo-PC
"""
import sys
import json
import math 

# fr: Frecuencia de la palabra en el documento
# vr: Vector resultante. 
def tf(vector_space,idf):
    tfidf = {} 
    for key, value in vector_space.items():
        vr = []
        for id, fr in enumerate(value):
            if fr > 0:
                v_tfIdf = fr*idf[id]
            else:
                v_tfIdf = 0
            vr.append(v_tfIdf)
        tfidf[key] = vr   
    return tfidf

def idf (palabras,noticias,indiceInvertido):
    longitud = len(noticias)
    v_idf = []
    for indice in indiceInvertido.values():
        inv_frec = math.log10(longitud/len(indice))   
#        print(len(indice))           
        v_idf.append(inv_frec) 
    return v_idf

def main(args): 
# -----------------------
# Obtenemos el documento
    Json_noticia = []
    noticias  = open(r'Doc\noticias.txt', "r")
    Json_noticia = json.JSONDecoder().decode(noticias.read())
# Obtenemos el diccionario 
    Json_palabra = []
    palabras  = open(r'Doc\palabras.txt', "r")
    Json_palabra = json.JSONDecoder().decode(palabras.read())
# Obtenemos el diccionario 
    vsx = []
    vs  = open(r'Doc\VectorSpace.txt', "r")
    vsx = json.JSONDecoder().decode(vs.read())
    
    # Obtenemos el diccionario 
    Json_indiceInvertido = []
    indiceInvertido  = open(r'Doc\Indice_invertido.txt', "r")
    Json_indiceInvertido = json.JSONDecoder().decode(indiceInvertido.read())
# -----------------------
    
    v_idf = idf(Json_palabra,Json_noticia,Json_indiceInvertido)
    
    IdfText = open(r'Doc\idf.txt', "w")
    IdfText.write(json.JSONEncoder().encode(v_idf))
    
    v_tfIdf = tf(vsx,v_idf)
    
    tfIdfText = open(r'Doc\TfIdf.txt', "w")
    tfIdfText.write(json.JSONEncoder().encode(v_tfIdf))
    

if __name__ == '__main__': 
    main(sys.argv)
