def suiv(joueur):
    if joueur==0:
        return 1
    elif joueur==1:
        return 0

def grille_vide():
    M = [[],[],[],
         [],[],[],
         [],[],[]]
    return M

def affiche_grille(grille,message):
    if message=="Rappel de l'historique des tirs que vous avez effectués :":
        print(message)
        gri=[]
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                grille[i][j].append(" | ")
            grille[i][j].append(" | ")

    elif message=="Découvrez votre grille de jeu avec vos bateaux : ":



def demande_position():
    while True:
        pos=(input("Entrez la position (ligne,colonne) entre 1 et 3: "))
        bon=[1,2,3]
        if pos[0].isdigit() and pos[2].isdigit():
            ligne = pos[0]
            colone=pos[2]
            if int(ligne) in bon and int(colone) in bon:
                break
    tup=(int(ligne),int(colone))
    return tup