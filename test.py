from random import *
from time import sleep
def grille_vide():
    M = [[],[],[],
         [],[],[],
         [],[],[]]
    return M

def affiche_grille(grille,message):
    if message=="Rappel de l'historique des tirs que vous avez effectués :":
        print(message)
        gri=grille
        for i in range(len(gri)):
            for j in range(len(gri[i])):
                gri[i][j].append(" | ")
            gri[i].append(" | ")
        print(gri)


print(affiche_grille(grille_vide(),"Rappel de l'historique des tirs que vous avez effectués :"))