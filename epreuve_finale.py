import random
from time import sleep
import json

def charger_indices(fichier):
    with open(fichier, "r", encoding='utf-8') as f:
        indice_salle={}
        donnees = json.load(f)
        print(donnees.values())
        print(donnees.keys())
        for i in donnees.values():
            for w in i.values():
                for z in w.values():
                    print(z,"\n")
    return indice_salle



def salle_de_tresor():
    fichier = 'indicesSalles.json'
    with open(fichier, "r", encoding='utf-8') as f:
        indice_salle = {}
        tempo = []
        donnees = json.load(f)
    for i in donnees.values():
        for j in donnees["Fort Boyard"].keys():
            tempo.append(j)
    annee = str(random.choice(tempo))
    tempo = []
    for w in donnees["Fort Boyard"][annee].keys():
        tempo.append(w)
    emission = str(random.choice(tempo))
    tempo = []
    #for i in donnees["Fort Boyard"][annee][emission].keys():

    return emission

print(salle_de_tresor())