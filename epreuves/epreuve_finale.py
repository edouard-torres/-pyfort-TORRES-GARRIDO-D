import random
from time import sleep
import json
from time import sleep

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
    fichier = 'data/indicesSalles.json'
    with open(fichier, "r", encoding='utf-8') as f:
        indice_salle = {}
        tempo = []
        jeu_tv = json.load(f)
    for i in jeu_tv.values():
        for j in jeu_tv["Fort Boyard"].keys():
            tempo.append(j)
    annee = str(random.choice(tempo))
    tempo = []
    for w in jeu_tv["Fort Boyard"][annee].keys():
        tempo.append(w)
    emission = str(random.choice(tempo))
    tempo = []
    for i in jeu_tv["Fort Boyard"][annee][emission].values():
        tempo.append(i)
    mot_code = tempo[1]
    indices = tempo[0]



    print(f"\n\nVoici les trois premiers indices du mot code :\n" )
    sleep(1)
    for i in range(3):
        print(indices[i],'\n')
        sleep(1)
    essais = 3
    rep_correcte = False
    n = 3
    while essais > 0 and rep_correcte == False:
        rep = input("\nÀ votre avis et à l'aide des indices, quel est le mot code ?\n").upper()
        if rep == mot_code:
            rep_correcte = True
        else:
            essais -= 1
            if essais > 0:
                print(f"Il vous reste {essais} essais\n")
                sleep(1)
                print(f"\nVoici un indice en plus pour vous aider dans votre quête du mot code :\n")
                sleep(1)
                print(indices[n],'\n')
            else:
                print(f"\nVous n'avez plus d'essais, le mot code était\n")
                sleep(1)
                print(mot_code)
        n += 1
    if rep_correcte == True:
        return "\nBRAVO ! Vous avez gagné !"
    else:
        return "DOMMAGE ! A l'année prochaine :)"


