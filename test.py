def tour(joueur, grille_tirs_joueur, grille_adversaire) :
    if joueur == 0:
        print("C'est à votre tour de faire feu !:")
    else:
        print("C'est le tour du maître du jeu :")

    affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")

    if joueur == 0:
        ligne, colonne = demande_position()
    else:
        ligne, colonne = random.randint(0, 2), random.randint(0, 2)
        print(f"Le maître du jeu tire en position {ligne + 1},{colonne + 1}")

    if grille_adversaire[ligne][colonne] == 'B':
        print("Touché coulé !")
        grille_tirs_joueur[ligne][colonne] = 'x'
        grille_adversaire[ligne][colonne] = ' '
    else:
        print("Dans l'eau...")
        grille_tirs_joueur[ligne][colonne] = '.'