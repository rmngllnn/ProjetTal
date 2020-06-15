from Fonctions import *
import sys

'''
A LANCER AVEC UN NOM DE FICHIER EN ARGUMENT
'''

import matplotlib.pyplot as plt


def similarite(dicoTrain, language) :
    fileName = 'variables/' + language + 'Dico.pkl'
    data = open(fileName, 'rb')
    dicoCorpus = pickle.load(data)
    data.close()
    return similariteCosinus(dicoCorpus, dicoTrain), similariteDistanceEuclidienne(dicoCorpus, dicoTrain)

def maxSim(liste) :
    indMax = 0
    for i in range (0, len(liste)) :
        if liste[i] > liste[indMax] :
            indMax = i
    return indMax

if len(sys.argv) > 1 :
    txt = readFile(sys.argv[1])
    txt = numb_less(txt)
    dicoTrain = createDico(txt)

    simListCos, simListDE = [], []
    simAllCos, simAllDE = similarite(dicoTrain, "Allemand")
    simListCos.append(simAllCos)
    simListDE.append(simAllDE)
    simAngCos, simAngDE = similarite(dicoTrain, "Anglais")
    simListCos.append(simAngCos)
    simListDE.append(simAngDE)
    simEsCos, simEsDE = similarite(dicoTrain, "Espagnol")
    simListCos.append(simEsCos)
    simListDE.append(simEsDE)
    simFrCos, simFrDE = similarite(dicoTrain, "Francais")
    simListCos.append(simFrCos)
    simListDE.append(simFrDE)
    simPtCos, simPtDE = similarite(dicoTrain, "Portugais")
    simListCos.append(simPtCos)
    simListDE.append(simPtDE)

    print("Allemand : cos ->", simAllCos, "DE ->", simAllDE)
    print("Anglais : cos ->", simAngCos, "DE ->", simAngDE)
    print("Espagnol : cos ->", simEsCos, "DE ->", simEsDE)
    print("Francais : cos ->", simFrCos, "DE ->", simFrDE)
    print("Portugais : cos ->", simPtCos, "DE ->", simPtDE)

    indCos = maxSim(simListCos)
    indDE = maxSim(simListDE)

    langages = ["Allemand", "Anglais", "Espagnol", "Francais", "Portugais"]
    print()
    print("D'après le cosinus, le texte semble être en", langages[indCos])
    print("D'après la distance euclidienne, le texte semble être en", langages[indDE])
