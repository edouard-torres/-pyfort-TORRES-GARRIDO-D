from operator import truediv
from random import *
from time import *

def suiv(joueur):
    if joueur == 0:
        return 1
    else:
        return 0

def grille_vide():
    M = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
    return M

def affiche_grille(grille,message):
    print(message)
    for ligne in grille:
        print("| {} | {} | {} |".format(*ligne))
    return 13*'-'

def demande_position():
    verif = True
    while verif:
        pos=(input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2): "))
        bon=[1,2,3]
        if len(pos)==3:
            if pos[0].isdigit() and pos[2].isdigit():
                ligne = pos[0]
                colone= pos[2]
                if int(ligne) in bon and int(colone) in bon:
                    verif = False
                    tup=(int(ligne)-1,int(colone)-1)
                    return tup

def init():
    grille = grille_vide()
    for i in range(2):
        verif = True
        while verif:
            coord_bateau = demande_position()
            l=coord_bateau[0]
            c=coord_bateau[1]
            #print("l:",l,"c:",c)
            if grille[l][c]==" ":
                grille[l][c]='B'
                verif = False
            else:
                print("Impossible de placer un bateau ici car l'emplacement est déjà pris.\n")
    return grille

def get_position(joueur):
    if joueur==0:
        return demande_position()
    elif joueur==1:
        return  (randint(0,2),randint(0,2))


def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur==0:
        print("\nC'est à votre tour de faire feu ! \n")
        print(affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués : "))
    else:
        print("\nc'est maintenant au maitre du jeu de jouer\n")
        print(affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que le maitre du jeu à effectués : "))

    sleep(1)
    sleep(1)
    verif = True
    while verif:
        position = get_position(joueur)
        l=position[0]
        c=position[1]
        if grille_tirs_joueur[l][c]==" ":
            verif = False
            print("\nun tir va être effectuer en ",l+1,",",c+1,"\n")
            sleep(1)
    if grille_adversaire[l][c]=="B":
        print("Touché coulé !\n")
        grille_tirs_joueur[l][c]="X"
        grille_adversaire[l][c]="X"
    else:
        print("PLOUF !\n")
        grille_tirs_joueur[l][c]="."
        grille_adversaire[l][c]="."
    sleep(2)



def gagner(grille_tirs_joueur):
    compt=0
    for i in grille_tirs_joueur:
        for j in i:
            if j=="X":
                compt+=1
    if compt==2:
        return True
    else:
        return False
def ecriture():
    print("Bienvenue dans le jeu bataille navale!")
    sleep(1)
    print("Dans ce jeu vous affronterez le maitre du jeu.")
    sleep(2)
    print("Chacun d'entre vous devra placer 2 bateau sur une grille de 3x3")
    sleep(2)
    print("Les bateaux sont représentés par 'B'")
    sleep(2)
    print("les tirs manqués par '.'")
    sleep(2)
    print("et les bateaux coulés sont marqués par 'X'.\n")
    sleep(1)

def jeu_bataille_navale():
    #print("Bienvenue dans le jeu bataille navale!\nDans ce jeu vous affronterez le maitre du jeu.\nChacun d'entre vous devra placer 2 bateau sur une grille de 3x3\nLes bateaux sont représentés par 'B'\nles tirs manqués par '.'\net les bateaux coulés sont marqués par 'X'.\n")
    ecriture()
    grille_bateau_joueur=init()
    print(affiche_grille(grille_bateau_joueur,"\nvoici l'emplacement de vos bateau"))

    grille_bateau_ordinateur=grille_vide()
    grille_bateau_ordinateur[randint(0,2)][randint(0,2)]="B"
    verif=True
    while verif:
        a=randint(0,2)
        b=randint(0,2)
        if grille_bateau_ordinateur[a][b]==" ":
            grille_bateau_ordinateur[a][b]="B"
            verif = False
    grille_tirs_joueur = grille_vide()
    grille_tirs_ordinateur = grille_vide()
    joueur = 0
    jeu=True
    while jeu:
        #       pour tricher     print("\n", affiche_grille(grille_bateau_ordinateur,"table ordinateur\n"))
        tour(joueur,grille_tirs_joueur,grille_bateau_ordinateur)
        if gagner(grille_tirs_joueur):
            jeu = False
            print("vous avez gagné\n")
            return True
        joueur=1
        tour(joueur,grille_tirs_ordinateur,grille_bateau_joueur)
        if gagner(grille_tirs_ordinateur):
            jeu=False
            print("vous avez perdue\n")
            sleep(1)
            print(affiche_grille(grille_bateau_ordinateur,"les bateaux du maitre du jeu étaient ici"),"\n")
            return False
        joueur=0


jeu_bataille_navale()


