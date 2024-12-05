import random

def factorielle(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return(x)

def epreuve_math_factorielle():
    n = random.randint(1,10)
    solution = input("Donner le résultat de "+str(n)+" factorielle:")
    rep = factorielle(n)
    if str(solution) == str(rep):
        return True
    else:
        return False

def est_premier(n):
    premier = True
    for i in range(2,n):
        if n%i == 0:
            premier = False
    return(premier)

def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n

def epreuve_math_premier():
    n = random.randint(10,20)
    solution = input("Trouver le nombre premier le plus proche de "+str(n)+" : ")
    rep = premier_plus_proche(n)
    if str(solution) == str(rep):
        print(f"Bravo ! C'était bien {solution} ! Ton équipe gagne une clé.")
        return True
    else:
        print(f"Dommage ! le nombre premier le plus proche de {n} est {rep}")
        return False

def epreuve_roulette_mathematique():
    nb=[]
    for i in range (5):
        nb.append(random.randint(1,20))
    list=['addition','soustraction','multiplication']
    signe=random.choice(list)
    if signe=='addition':
        resultat=0
        for i in nb:
            resultat+=i
    elif signe=='soustraction':
        resultat=nb[0]
        for i in range(1,len(nb)):
            resultat-=nb[i]
    elif signe=='multiplication':
        resultat=1
        for i in nb:
            resultat*=i
    print("Nombre sur la roulette: ",nb)
    print("Calculez le résultat en combinant ces nombres avec une",signe)
    reponse=int(input("Votre réponse: "))
    if str(reponse)==str(resultat):
        return True
    else:
        return False


def epreuves_maths():
    epreuves = [epreuve_math_factorielle,epreuve_math_premier,epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    reussi = epreuve()
    if reussi:
        print("Bravo, vous venez de gagner une clé")

epreuves_maths()
