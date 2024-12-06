from random import*
from time import sleep
import json


def charger_indices(fichier):
    with open(fichier, "r", encoding='utf-8') as f:
        indice_salle={}
        donnees = json.load(f)
        print(donnees.values())
        print(donnees.keys())
        for i in donnees.values():
            for j in i:
                print(j,"\n")
            #indice_salle[i['Indices']]=i['MOT-CODE']
    return indice_salle



def salle_De_Tresor():
    print()


print(charger_indices("indicesSalles.json"))