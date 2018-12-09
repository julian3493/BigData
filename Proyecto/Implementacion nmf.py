# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:39:40 2018

@author: Julian
"""

from __future__ import print_function
from time import time

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from nltk.corpus import stopwords

n_samples = 1000
n_features = 1000
n_topics = 10
n_top_words = 10
noticia_max=[]
t0 = time()
var=0

# Cargar el archivo del conjunto de datos
archivoNoticias=open(r'Doc\noticiasPuritas.txt', "r")
dataset=json.JSONDecoder().decode(archivoNoticias.read())
archivoNoticias.close()

lista=[]
for id, noticia in dataset.items():
    lista.append(noticia)

vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, max_features=n_features,
                             stop_words=stopwords.words("spanish"))
tfidf = vectorizer.fit_transform(lista[:n_samples])
print("tf-idf hecha en %0.3fs." % (time() - t0))

#nmf
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
print("nmf hecha en %0.3fs." % (time() - t0))
otranmf=NMF(n_components=n_topics, random_state=1).fit_transform(tfidf)

print(nmf.components_.shape)
print(otranmf.shape)
feature_names = vectorizer.get_feature_names()

print("**************************************************")
for j in range(5):
    n_max=0
    for i in range(498):
        if otranmf[i][j]>n_max:
            n_max=otranmf[i][j]
            var=i
    noticia_max.append(var)

        

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    
print(noticia_max)

for key in noticia_max: 
    print()
    print(key)
    print(dataset[str(key)])
    
#xx = open(r'Doc\Indice_invertido.txt', "w")
#xx.write(json.JSONEncoder().encode(indiceInvertido))
#xx.close()

    


    
#for topic_idx, topic in enumerate(otranmf):
#    print("Topic #%d:" % topic_idx)
#    print(" ".join([feature_names[i]
#                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    
