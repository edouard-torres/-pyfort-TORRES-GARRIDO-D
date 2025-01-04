pyfort TORRES GARRIDO D4

Bienvenue dans notre rojet intitulé 'Pyfort'. En démarant ce code, vous allez rentrer sur le célèbre fort boyard (revisité bien sûr). Votre but: réussir les épreuves afin d'obtenir 3 clées.


tous les pushs ont été fait par edouard car nous avons travaillé tous les 2 grâce au "code with me" de pycharm. Vous pouvez par ailleurs remarquer que nous avons 1 méthode différente de coder chacun.

fonctionnalités principales:
- un choix d'équipe allant jusqu'à 3 joueurs personnalisé (nom, proféssion et choix du leader)
- un choix d'épreuves riches et variées
- une sensation d'être sur le vrai fort
- une sauvegarde de données


tout le programme a été fait en python et grâce aux bibliothèques:
- Time
- Random
- Math
- Colorama (qu'il faut installer)
- json

le tout sur pycharm windows

Pour lancer le programmes, il faut lancer le main et simplement suivre les explications.


epreuve_final.py:
- charger_indice() que nous n'avons pas uttilisé (mais qui était demandé)
- salle_de_tresor() si l'équipe possède 3 clées, cette fonction se lance et l'équipe doit déchiffrer le code nécessaire pour ouvrir la porte afin d'accéder au
trésor.

epreuves_hasard.py:
- beau_bonneteau() un print qui sert à afficher des bonneteaux.
- bonneteau() [epreuve] où le joueur doit retrouver une "balle" caché sous l'un des 3 bonneteaux (il possède 2 tentatives pour cela).
- jeu_lance_des() [epreuve] où le joueur affronte le maitre du jeu, chacun lance 2 dés et si l'un des deux fait au moins un 6 il gagne (il y a 3 tours maximum).
- course() [epreuve] qui est un jeux de hasard que nous avons rajouté et qui comme son nom l'indique est une course de chevaux où le joueur doit parier sur la victoire d'un cheval.
- epreuve_hasard() qui sert à executer aléatoirement un des jeux cité plus haut.


epreuve_logiques.py
- pour la bataille navale [epreuve]:
  - suiv() qui n'est pas uttlisé mais qui devais servir à changer le joueur (entre l'ordinateur et le joueur)
  - grille_vide() qui sert à renvoyer une grille vide
  - affiche_grille() qui sert à afficher une grille en 3x3
  - demande_position() qui sert à faire une saisie sécurisé
  - init() qui sert à initialiser la grille des bateaux avec demande_position()
  - get_position() qui demande_position() quand c'est le joueur et qui donne des positions aléatoires si c'est l'ordinateur
  - tour() qui sert à faire un tour du joueur et du bot
  - gagner() qui sert à vérifier si le joueur à gagné ou non
  - écriture() qui sert à écrire les règles au lancement de la bataille navale
  - mode_jeux() qui sert à demander si le joueur veux jouer en mode rapide(sans les sleep) ou en normal (avec les sleep)
  - jeu bataille_navale() qui execute tous ces programmes afin de jouer à la bataille navale
- epreuves_guess [epreuve] qui est une autre epreuve que nous avons rajouté où l'on dois deviner un nombre entre 1 et 100 (tentative limité)
- pour le mémory [epreuve que nous avons rajouté également]:
  - retranscripption() qui sert à transformer un nombre entre 0 et 15 en coordonnée pour une matrice en 4x4
  - init_memory() qui sert à remplir une matrice 4x4 avec des fruits (emojis)
  - verif_memory() qui sert à vérifier si il reste des 'X' dans une matrice (cela sert à savoir si le joueur a gagné)
  - saisie_memory() qui sert à faire une saisie sécurisé de deux coordonnées
  - affichage_mémory() qui sert à afficher proprement une matrice de 4x4
  - tour mémory() qui sert à effectuer un tour de jeu
  - memory() qui regroupe les fonctions ci-dessus
- epreuve_logik() qui sert à executer un des jeux cité plus haut de façon aléatoire


epreuves_mathématiques.py
- factoriel() qui sert à calculer la factoriel d'un nombre.
- epreuve_math_factoriel() [epreuve] où le joueur doit donner une factorielle d'un nombre choisir de manière aléatoire entre 1 et 10 + vérifie si la réponse donnée est bonne
- est_premier() vérifie si un nombre est premier
- premier_plus_proche() sert à connaitre le chiffre premier le plus proche d'un autre chiffre premier
- epreuve_math_premier() [epreuve] où le joueur doit rentrer le nombre premier le plus proche d'un nombre choisi de manière aléatoire entre 10 et 20.
- epreuve_roulette_math() [epreuve] où une suite de 5 entier est générée et où le joueur doit les additionner, les soustraire ou les multiplier + vérifie si sa réponse est correcte
- epreuve_carre() [epreuve] est une epreuve que nous avons rajouté où le joueur dois rentrer le carré d'un nombre choisi entre 1 et 10.
- verif_table() [epreuve] est une epreuve que nous avons rajouté où le joueur doit donner la/les table(s) (entre 1 et 10) de multiplication dans laquelle se trouve un certain nombre (compris entre 1 et 100).
- epreuve_maths() qui sert à executer aléatoirement un des jeux cité plus haut


enigme_pere_fouras.py
- charger_enigme() qui sert à charger les questions et les réponses des enigmes depuis un fichier .json
- get_question_reponse() qui choisie un couple "question reponse" aléatoirement dans la liste du fichier .json
- belle_question() qui sert à faire en sorte que la question soit plus jolie à l'affichage
- enigme_pere_fouras() [epreuve] qui pose la question du père fouras au joueur.

fonction_utiles.py
- ecriture_de_fou() qui sert à ecrire un texte de façon stylée (mais qui n'a pas été uttilisé)
- introduction() qui sert à écrire l'introduction et les consignes du jeu
- nb_joueur() qui permet de choisir le nombre de joueur pour la partie (entre 1 et 3)
- composer_equipe() qui sert à rentrer les noms, profession et statut (chef ou non) des joueurs
- menue_epreuves() qui sert à choisir le type d'epreuve que l'équipe souhaite jouer
- choisir_joueur() qui sert à choisir un joueur à envoyer jouer à une epreuve

main.py
- qui regroupe tous les fichier .py ci-dessus et les lancent

stockage_données.py
- stockage() qui sert à stocker des informations dans le dossier données.txt sur la partie qui a été joué, avec le temps que cela a prit

Gestion des Entrées et Erreurs :
- Mise en place d'une saisie sécurisé pour toutes les saisies clavier (via l'utilisation de .isdigit(), .split('.'), des listes contenant les saisies attendues      qui force le joueur à rentrer une des valeur de la liste), cela nous a permis d'éviter toutes les erreurs de types "type error" et d'éviter de devoir sans cesse 
  relancer le programme et de perdre la progression du jeu

Chronologie du Projet :
- visible directement depuis les commits de edouard torres (sur son compte github : https://github.com/edouard-torres)

Répartition des Tâches :
- On a fait le projet dans l'ordre du pdf, on faisait chacun une fonction différente en même temps tout en s'entraidant si besoin.

Stratégies de Test :
- Mise en place de print() un peu partout (afin de débugger les fonctions si besoin)
- Ajout d'assertion (pour vérifier si nos paramètre en entrée étaient valide)



