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



def salle_De_Tresor():
    fichier = 'indicesSalles.json'
    with open(fichier, "r", encoding='utf-8') as f:
        indice_salle={}
        donnees = json.load(f)
    for i in donnees.values():
        for j in i.keys():
            print(j)

salle_De_Tresor()