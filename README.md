pyfort TORRES GARRIDO D4

Bienvenue dans notre rojet intitulé 'Pyfort'. En démarant ce code, vous allez rentrer sur le célèbre fort boyard (revisité bien sûr). Votre but: réussir les épreuves afin d'obtenir 3 clées.


tous les pushs ont été fait par edouard car nous avons travaillé tous les 2 grâce au "code with me" de pycharm. Vous pouvez remarquer que nous avons 2 méthodes différentes de coder pour le prouver 

fonctionalité principale:
- un choix d'équipe allant jusqu'a 3 joueurs personalisé (nom, proféssion et choix du leader)
- un choix d'épreuves riches et varié
- une sensation d'être sur le vrai fort
- une sauvegarde de données


tout le programme a été fait en python et grâce aux bibliothèques:
- Time
- Random
- Math
- Colorama (qu'il faut installer)
- json

le tout sur pycharm windows

Pour lancer le programmes, il faut lancer le main et c'est tout et suivre les explications.


epreuve_final.py:
- charger indice() que nous n'avons pas uttiliser
- salle_de_tresor() qui nous sert a donner 3 indices puis 2 autres.

epreuves_hasard.py:
- beau_bonneteau() qui sert à afficher des beau bonneteau
- bonneteau() qui est un des jeux de hasard
- jeu_lance_des qui est le deuxième jeux
- course() qui est un jeux bonus ou l(on parie sur un cheval
- epreuve_hasard() qui sert a executer aléatoirement un des jeux cité plus haut


epreuve_logiques.py
- pour la bataille navale:
  - suiv() qui n'est pas uttliser mais qui devais servir à changer le joueur (entre l'ordinateur et le joueur)
  - grille_vide() qui sert à renvoyer une grille vide
  - affiche_grille() qui sert à afficher une grille en 3x3
  - demande_position() qui sert à faire une saisie sécuriser
  - init() qui sert à initialiser la grille des bateau avec demande_position()
  - get_position() qui demande_position() quand c'est le joueur et qui donne des positions aléatoires si c'est l'ordinateur
  - tour() qui sert à faire un tour du joueur et du bot
  - gagner() qui sert à vérifie si le joueur a gagner ou non
  - écriture() qui sert à écrire les règles au lancement de la bataille navale
  - mode_jeux() qui sert à demander si le joueur veux jouer en mode rapide(sans les sleep) ou en normal (avec les sleep)
  - jeu bataille_navale() qui execute tout ces programmes afin de jouer a la bataille naval
- epreuves_guess qui est une autre epreuves ou l(on dois deviner un nombre entre 1 et 100
- pour le mémory:
  - retranscripption() qui sert à transformer un nombre entre 0 et 15 en coordonée pour une matrice en 4x4
  - init_memory() qui sert à remplir une matrice 4x4 avec des fruits
  - verif_memory() qui sert à vérifier si il reste des 'X' dans une matrice (cela sert a savoir si le joueur a gagner)
  - saisie_memory() qui sert à faire une saisie sécuriser de deux coordonées
  - affichage_mémory() qui sert à afficher proprement une matrice de 4x4
  - tour mémory() qui sert à effectuer un tour de jeux
  - memory() qui regroupe les fonctions ci dessus
- epreuve_logik() qui sert à executer un des jeux cité plus haut aléatoirement


epreuves_mathématiques.py
- factoriel qui sert à calculer la factoriel d'un nombre
- epreuve_math_factoriel() qui sert à demander une factoriel aléatoire entre 1 et 10 puis la calcul et vérifie si la réponse donnée est bonne
- est_premier() vérifie si un nombre est premier
- premier_plus_proche() sert à connaitre le chifre premier le plus proche d'un autre chifre premier
- epreuve_math_premier() est le premier jeux qui sert à demander de rentrer le nombre premier le plus proche d'un nombre aléatoire entre 10 et 20
- epreuve_roulette_math() est le second jeux qui genere une suite de 5 entier et demande a l'uttilisateur de les additioner, les soustraire ou les multiplier et vérifie si ca réponse est correcte
- epreuve_carre() est une epreuve ou l'uttilisatuer dois rentrer le carré d'un nombre entre 1 et 10 qui est ensuite vérifier par l'ordinateur
- verif_table() qui est une autre épreuve ou l'on dois donner dans quelle table se trouve un certain nombre( qui est ensuite vérifier par l'ordinateur encore une fois)
- epreuve_maths() qui sert a executer aléatoirement un des jeux cité plus haut


enigme_pere_fouras.py
- charger_enigme() qui sert à charger les questions et les réponses des enigmes depûis un fichier json
- get_question_reponse() qui choisie un couple question reponse aléatoirement dans la liste ci dessus
- belle_question() qui sert à faire en sorte que la question soit plus jolie a l'affichage
- enigme_pere_fouras() qui pose la question du pere fouras

fonction_utiles.py
- ecriture_de_fou() qui sert à ecrire un texte de façon stylée (mais qui n'a pas été uttiliser)
- introduction() qui sert à écrire l'introduction et les consigne du jeux
- nb_joueur() qui permet de choisir le nombre de joueur pour la partie (entre 1 et 3)
- composer_equipe() qui sert à rentrer les noms, profession et statut (chef ou non) des joueurs
- menue_epreuves() qui sert à choisir le type d'epreuve que l'uttilisateur veux
- choisir_joueur() qui sert à choisir un joueur a envoyer à une epreuve

main.py
- qui regroupe toute les fichier .py ci dessus et les lance

stockage_données.py
- stockage() qui sert à stocker des information dans le dossier données.txt sur la partie qui a été joué, avec le temps que cela a prit







