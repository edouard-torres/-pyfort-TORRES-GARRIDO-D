from random import *
from time import sleep



def bonneteau():
    reussi = False
    tentative = 0
    L = ['A','B','C']
    bon_choix = choice(L)
    choix_joueur = input("Choisissez le bonneteau sous lequel se cache la clé (A,B ou C) : ")
    while reussi == False and tentative < 1:
        if ord(choix_joueur) >= 97 and ord(choix_joueur) <= 122:
            choix_joueur = chr(ord(choix_joueur) - 32)
        if bon_choix == choix_joueur:
            reussi = True
        else:
            bon_choix = choice(L)
            print("La clé ne se trouvait pas sous ce bonneteau.")
            choix_joueur = input("Choisissez le bonneteau sous lequel se cache la clé (A,B ou C) : ")
        tentative += 1
    if reussi == True:
        print("Bravo ! Vous avez choisi le bon bonneteau et vous obtenez une clé !")
        return True
    else:
        print("Dommage !")
        return False

def jeu_lance_des():
    nb_essai=3
    for essai in range(3):
        print("il reste ",3-essai,"essai.")
        input("appuyer sur entrer pour lancer les dés   ")
        dés_joueur =(randint(1,6),randint(1,6))
        print("vous avez eu",dés_joueur[0],"et",dés_joueur[1],"\n")
        sleep(1)
        for i in dés_joueur:
            if i==6:
                sleep(1)
                print("vous avez gagner la partie et la clé")
                return True
        dés_maitre =(randint(1,6),randint(1,6))
        print("le maitre du jeux a eu",dés_maitre[0],"et",dés_maitre[1],"\n")
        sleep(1)
        for i in dés_maitre:
            if i==6:
                sleep(0.5)
                print("le maitre du jeux a remporter la partie")
                return False
        if essai!=3:
            print("on passe au prochain essai \n")
        sleep(0.5)
    print("aucun joueur n'a obtenue de 6 \n")
    return False

def epreuves_hasard():
    epreuves = [bonneteau,jeu_lance_des]
    epreuve = choice(epreuves)
    reussi = epreuve()
    if reussi:
        print("Bravo, vous venez de gagner une clé")

epreuves_hasard()