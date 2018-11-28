# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:22:15 2018

-- Se obtiene la informacion del documento .sgm (Titulo y Cuerpo)
    y se representa en un arreglo de palabras listo para procesar. 

@author: Leonardo-PC
"""
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from bs4 import BeautifulSoup
import json
import sys

# VARIABLES
#------------------------------------------------------------------------------
  # Variables contador
noticias = varTitle = varBody = ""                  # VARIABLES PARA ALMACENAR RESULTADOS 
listNoticias = {} 
listPalabras = list()
stop_words = set(stopwords.words('english')) 
#------------------------------------------------------------------------------
def main(args):
    # Contador de item's 
    contadorReuter = 0 
    # Abrir documento y realizar el parseo a un HTML
    f = open(r'Doc\reut2-000.sgm', 'r')
    data= f.read()
    soup = BeautifulSoup(data,'html.parser')
    
    
    # Extraer infromacion del titulo y del body 
    for r in soup.find_all('reuters'):
        contadorReuter+= 1
        for t in r.find_all('title'):
            varTitle = t.string
        for b in r.find_all('body'):
            varBody = b.string
        noticias = varTitle.lower() +" "+ varBody.lower()
    
    # Utilizar tokenize para splitear  noticia y agregarla a la lista resultante
        palabras = word_tokenize(noticias)
        linea = list()
        for r in palabras :
            
            if re.match("[0-9,->]",r) or re.match("\x03",r):
                continue
            if not r in stop_words:
                 linea.append(r)
                 if r not in listPalabras:
                     listPalabras.append(r)
        listNoticias[contadorReuter] = linea
            
    # arreglo de las palabras por noticias
    palabrasD1 = open(r'Doc\noticias.txt', 'w')
    palabrasD1.write(json.JSONEncoder().encode(listNoticias))
    palabrasD1.close
    
    # arreglo de palaras (sin repetir)
    palabrasD2 = open(r'Doc\palabras.txt', 'w')
    palabrasD2.write(json.JSONEncoder().encode(listPalabras))
    palabrasD2.close


# metodo main
if __name__ == '__main__':
    main(sys.argv)



















