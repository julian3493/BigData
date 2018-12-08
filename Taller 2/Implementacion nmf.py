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
n_top_words = 15

t0 = time()

# Cargar el archivo del conjunto de datos
palabras=open(r'noticias.txt', "r")
dataset=json.JSONDecoder().decode(palabras.read())
palabras.close()

lista=[]
for id, noti in dataset.items():
    lista.append(noti)

#Tf-Idf
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                             stop_words='english')
tfidf = vectorizer.fit_transform(lista[:n_samples])
print("tf-idf hecha en %0.3fs." % (time() - t0))

#nmf
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
print("nmf hecha en %0.3fs." % (time() - t0))



feature_names = vectorizer.get_feature_names()

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))