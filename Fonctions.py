#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:19:26 2020

@authors: Romane GALLIENNE, Cindy PEREIRA, Nadège DEMANEE
"""

import string as str
from nltk import bigrams
import numpy as np

"""
Questionnement : est-ce qu'on ferait pas une fonction nettoyage (comme en JAVA)
pour enlever tout ce qui nous gêne (ponctuation, signes API), et qu'on peut
modifier selon les petits trucs qu'on rencontre qui nous embête
"""


#Fonction qui enlève la ponctuation. Fonctionne
def punct_less(texte):
    for punct in str.punctuation:
        texte = texte.replace(punct, "")
    return texte

#Fonction qui enlève les signes API
def api_less(texte):
    pass


#Fonction qui enlève les nombres (utile ?). Fonctionne
def numb_less(texte):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for num in numbers :
        texte = texte.replace(num, "")
    return texte


#Génère une liste de bigramme (en tuple je crois)
def ngrams(texte) :
    txt_bigrams = list(bigrams(texte))
    return txt_bigrams


#print(ngrams("Republic of Afghanistan, is a landlocked country in South and Central Asia."))


def vectorisation (texte):
    list_ngrams = ngrams(texte)
    dict = {} #on crée un dictionnaire vide
    i = 0
    for gram in list_ngrams:
        if gram not in dict:
            dict[gram] = 0 #il crée la clé qui lui donne une valeur 
    for gram in dict:
        dict[gram] = np.zeros(len(dict)) #on crée des vecteurs nuls de longueur du dictionnaire
        dict[gram][i] = 1
        i = i+1
    vecteur = np.zeros(len(dict)) #on crée des vecteurs nuls de longueur du dictionnaire
    for gram in list_ngrams:
        vecteur += dict[gram]        
    return vecteur

print(vectorisation(ngrams("Republic of Afghanistan, is a landlocked country in South and Central Asia.")))
        

