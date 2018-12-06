import math
import json
from time import time
from collections import Counter
from nltk.tokenize import word_tokenize

Diccionario = []
DiccionarioTxt = open(r'Doc\palabras.txt', "r")
Diccionario = json.JSONDecoder().decode(DiccionarioTxt.read())
DiccionarioTxt.close()

stopwords = []
file_stopwords = open(r'Doc\stopwords.txt', "r", errors="replace")
stopwords = file_stopwords.read().split()
file_stopwords.close()



def Comparar(Noticia, palabra):
    coincidences = 0
    for palabraNoticia in Noticia:
        if palabraNoticia == palabra:
            coincidences = coincidences + 1
    return coincidences


def Similitud(vectorSpace1, vectorSpace2):
    numerator = 0 
    sumxx, sumyy = 0, 0
    for i in range(len(vectorSpace1)):
        x = vectorSpace1[i]
        y = vectorSpace2[i]
        sumxx += x*x
        sumyy += y*y
        numerator += x*y
    return numerator/math.sqrt(sumxx*sumyy)


inverdIndex = {}
file_inverdIndex = open(r'Doc\Indice_invertido.txt', "r")
inverdIndex = json.JSONDecoder().decode(file_inverdIndex.read())
file_inverdIndex.close()

print("Escribe la consulta -> ")
query = input()
t0 = time()



listQuery = []
for palabra in word_tokenize(query.lower()):  # split
    if palabra not in stopwords:
        listQuery.append(palabra)
histQuery = Counter(listQuery)

vectorSpace = []
for palabra in Diccionario:
    vectorSpace.append(Comparar(histQuery, palabra))


ifv = []
ifvText = open(r'Doc\idf.txt', "r")
ifv = json.JSONDecoder().decode(ifvText.read())
ifvText.close()

tfidf = []
for id, fr in enumerate(vectorSpace):
    x = 0
    if fr > 0:
        x = fr*ifv[id]
    tfidf.append(x)

# Aca con el index invertido
allTfidf = {}
file_words = open(r'Doc\TfIdf.txt', "r")
allTfidf = json.JSONDecoder().decode(file_words.read())
file_words.close()

cosSim = {}
for palabra in histQuery:
    if palabra in inverdIndex:  # si la palabra esta en el index invertido
        for key in inverdIndex.get(palabra):
            if key not in cosSim:
                calc = Similitud(tfidf, allTfidf[key])
                cosSim[key] = calc


print("Para el texto: " + query + "..... Los documentos mas semejantes son: ")
print()

contador = 0
for key in sorted(cosSim, key=cosSim.get, reverse=True):
    print("Documento: #%s, Similitud: %f" % (key,cosSim[key]))
    contador += 1

    if contador>5:
        break
        
