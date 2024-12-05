from random import  *

def nb_joueur():
    nombre=['1','2','3']
    n = input("Combien de joueurs ? ")
    while n not in nombre:
        n = input("Combien de joueurs ? ")
    return(int(n))

def equipe(n):
    ekip=[]
    for i in range(n):
        nom=input("rentrer un nom: ")
        ekip.append(nom)
    return (ekip)

