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

n_samples = 2000
n_features = 1000
n_topics = 20
n_top_words = 20

t0 = time()

# Cargar el archivo del conjunto de datos
palabras=open(r'..\Taller 1\Doc\palabras.txt', "r")
dataset=[]
dataset=json.JSONDecoder().decode(palabras.read())
print(dataset)

#Tf-Idf
vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, max_features=n_features,
                             stop_words='english')
tfidf = vectorizer.fit_transform(dataset)
print("tf-idf hecha en %0.3fs." % (time() - t0))

#nmf
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
print("nmf hecha en %0.3fs." % (time() - t0))



feature_names = vectorizer.get_feature_names()

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))