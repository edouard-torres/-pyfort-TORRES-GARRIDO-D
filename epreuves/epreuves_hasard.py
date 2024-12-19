from random import *
from time import sleep

def beau_bonneteau():
    print("    _______         _______         _______    ")
    print("   /       \\       /       \\       /       \\   ")
    print("  /         \\     /         \\     /         \\  ")
    print(" /     A     \\   /     B     \\   /     C     \\ ")
    print("|             | |             | |             |")
    print("|             | |             | |             |")
    print("------------------------------------------------")

def bonneteau():
    reussi = False
    tentative = 0
    L = ['A','B','C']
    beau_bonneteau()
    bon_choix = choice(L)
    choix_joueur = input("Choisissez le bonneteau sous lequel se cache la clé (A,B ou C) : ")
    while reussi == False and tentative < 1:
        choix_joueur.lower()
        if bon_choix == choix_joueur:
            reussi = True
        else:
            bon_choix = choice(L)
            print("La clé ne se trouvait pas sous ce bonneteau.\n")
            choix_joueur = input("Choisissez le bonneteau sous lequel se cache la clé (A,B ou C) : ")
        tentative += 1
    if reussi == True:
        print("Bravo ! Vous avez choisi le bon bonneteau, bravo\n")
        return True
    else:
        print("Dommage !\n")
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

def epreuve_hasard():
    epreuves = [bonneteau,jeu_lance_des]
    epreuve = choice(epreuves)
    reussi = epreuve()
    if reussi:
        return True
    else:
        return False

