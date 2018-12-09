import math
import json
from time import time
from collections import Counter
from nltk.tokenize import word_tokenize


DiccionarioTxt = open(r'Doc\palabras.txt', "r")
Diccionario = json.JSONDecoder().decode(DiccionarioTxt.read())
DiccionarioTxt.close()

stopwordsTxt = open(r'Doc\stopwords.txt', "r", errors="replace")
stopwords = stopwordsTxt.read().split()
stopwordsTxt.close()

invTxt = open(r'Doc\Indice_invertido.txt', "r")
indiceInvertido = json.JSONDecoder().decode(invTxt.read())
invTxt.close()

print("Escribe la consulta -> ")
query = "Dow Chemical Co said a judge on the New Jersey Superior Court for Monmouth County granted its Merrell Dow Pharmaceuticals Inc unit a motion for a directed verdict in its favor in a case alleging its morning sickness drug, Bendectin, caused a child's birth defects"
t0 = time()

PalabrasConsulta = []
for palabra in word_tokenize(query.lower()):  
    if palabra not in stopwords:
        PalabrasConsulta.append(palabra)
consulta = Counter(PalabrasConsulta)


vectorSpace = []
for palabra in Diccionario:
    coincidences = 0
    for palabraNoticia in consulta:
        if palabraNoticia == palabra:
            coincidences = coincidences + 1
    vectorSpace.append(coincidences)


ifvText = open(r'Doc\idf.txt', "r")
ifv = json.JSONDecoder().decode(ifvText.read())
ifvText.close()

tfidf = []
for id, fr in enumerate(vectorSpace):
    x = 0
    if fr > 0:
        x = fr*ifv[id]
    tfidf.append(x)



file_words = open(r'Doc\TfIdf.txt', "r")
test = json.JSONDecoder().decode(file_words.read())
file_words.close()

similitud = {}
for palabra in consulta:
    if palabra in indiceInvertido:  
        for key in indiceInvertido.get(palabra):
            if key not in similitud:
                m = 0 
                x, y = 0, 0
                for i in range(len(tfidf)):
                    x += pow(tfidf[i],2)
                    y += pow(test[key][i],2)
                    m += tfidf[i]*test[key][i]
                similitud[key] = m/math.sqrt(x*y)
                

noticiaTxt = open(r'Doc\noticiasPuritas.txt', "r")
n = json.JSONDecoder().decode(noticiaTxt.read())
noticiaTxt.close()


print("Para el texto: " + query + "..... Los documentos mas semejantes son: ")
print()



contador = 0
for key in sorted(similitud, key=similitud.get, reverse=True):
    print()
    print("Documento: #%s, Similitud: %f" % (key,similitud[key]))
    print()
    
    print('body>>>>>>>>>>> %s: ' % n[key])
    contador += 1

    if contador>5:
        break
t1 = (time()- t0)
print(t1)
        
