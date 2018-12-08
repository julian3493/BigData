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

n_samples = 1000
n_features = 1000
n_topics = 10
n_top_words = 10
noticia_max=[]
t0 = time()
var=0

# Cargar el archivo del conjunto de datos
archivoNoticias=open(r'noticias.txt', "r")
dataset=json.JSONDecoder().decode(archivoNoticias.read())
archivoNoticias.close()

lista=[]
for id, noticia in dataset.items():
    lista.append(noticia)

#Tf-Idf
vectorizer = TfidfVectorizer(max_df=0.95, min_df=0.05, max_features=n_features,
                             stop_words='english')
tfidf = vectorizer.fit_transform(lista[:n_samples])
print("tf-idf hecha en %0.3fs." % (time() - t0))

#nmf
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
print("nmf hecha en %0.3fs." % (time() - t0))
matriz_W=NMF(n_components=n_topics, random_state=1).fit_transform(tfidf)

#print(nmf.components_.shape)
#print(matriz_W.shape)
feature_names = vectorizer.get_feature_names()

print("**************************************************")
#Se guarda la noticia de mayor valor en un vector
for j in range(10):
    n_max=0
    for i in range(1000):
        if matriz_W[i][j]>n_max:
            n_max=matriz_W[i][j]
            var=i
    noticia_max.append(var)

        
#Se imprime las palabras mas relevantes del topic
for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    
print("*************************************************")

#Se imprime la noticia mas significativa del topic
for key in noticia_max: 
    print(key)
    print(dataset[str(key)])
