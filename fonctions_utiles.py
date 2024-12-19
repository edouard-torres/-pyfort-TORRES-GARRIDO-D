from time import sleep
from random import choice
from colorama import *


def ecriture_de_fou(phrase):
    fin=""
    compt=0
    back=chr(8)
    long = 0
    liste=[]
    lettre=["'",","," ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "â", "ä", "é", "è", "ê", "ë", "î", "ï", "ô", "ö", "ù", "û", "ü", "ÿ", "ç"]
    while compt!=len(phrase):
        #print(long,compt)
        letre=choice(lettre)
        if  phrase[compt]==letre and long==2:
            #print("la")
            fin+=letre
            compt += 1
            long=0
        elif phrase[compt]==letre and long!=2:
            #print("la", long)
            long+=1
            fin += letre + back
        else:
            fin+=letre+back
    for letter in fin:
        liste.append(letter)
    #print(liste)
    for letter in fin:
        print(Fore.GREEN+letter, end='')
        sleep(0.0001)

def introduction():
    print("bienvenue")
    print()
    print("votre mission, si toute fois vous l'acceptez, est d'accomplir des épreuves")
    print()
    print("en accomplissant chaque epreuves, vous obtiendrais des clées")
    print()
    print("quand vous obtiendrais 3 clées, vous aller acceder a la salle au trésors\n")
    sleep(2)


def nb_joueur():
    nombre=['1','2','3']
    n = input("Combien de joueurs ? ")
    while n not in nombre:
        n = input("Combien de joueurs ? ")
    return(int(n))

def composer_equipe(n):
    ekip= {}
    est_leader = ["OUI","NON"]
    leader_choisi = False
    for i in range(n):
        print()
        sleep(0.2)
        nom= input("rentrer un nom: ")
        sleep(0.2)
        profession = input(f"Quel est votre profession {nom} ? ")
        sleep(0.2)
        leader = input(f"Etes-vous le leader de cette équipe (oui ou non) ? ").upper()
        while leader not in est_leader:
            sleep(0.2)
            leader = input(f"Répondez à la question, êtes-vous le leader de cette équipe (oui ou non) ? ")
        if leader == "OUI" and leader_choisi == False:
            leader_choisi = True
            ekip[i+1] = {"nom": nom, "profession": profession, "grade": "Leader","clé_gagnées":0}
        else:
            ekip[i+1] = {"nom": nom, "profession": profession, "grade": "Membre","clé_gagnées":0}
    if leader_choisi == False:
        ekip[1]["grade"] = "Leader"
    return ekip

#print(composer_equipe(2))

def menue_epreuves():
    print("\n\n\n")
    print("1. Epreuves de mathématiques\n")
    print("2. Epreuves de logique\n")
    print("3. Epreuves du hasard\n")
    print("4. enigme du pere fouras\n")
    t=True
    while t:
        choix = input("choix : ")
        if choix.isdigit():
            if int(choix)>0 and int(choix)<5:
                t=False
    print("\n\n")
    return int(choix)


def choisir_joueur(equipe):
    joueur_unique = {}
    n = len(equipe)
    nb_joueur = []
    for val in range(1,n+1):
        nb_joueur.append(val)
    for joueur,info in equipe.items():
        print(joueur,".", info["nom"], "(",info["profession"],") - ",info["grade"])
        sleep(0.5)
    joueur_choisi = int(input("Entrez le numéro du joueur: "))
    while joueur_choisi not in nb_joueur:
        sleep(0.5)
        joueur_choisi = int(input("Entrez le numéro d'un joueur valide : "))
    joueur_unique[joueur_choisi] = equipe[joueur_choisi]
    print("\n\n")
    return joueur_choisi

