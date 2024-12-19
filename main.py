from epreuves.epreuve_finale import *
from epreuves.epreuves_hasard import *
from epreuves.epreuves_logiques import *
from epreuves.epreuves_mathematiques import *
from fonctions_utiles import *
from enigme_pere_fouras import *
from epreuves import *

cle_général = 0

if __name__ == '__main__':
    introduction()
    nombre_de_joueur=nb_joueur()
    equipe=composer_equipe(nombre_de_joueur)
    while cle_général!=3:
        print("\nVous avez ",cle_général,"clées en tout\n")
        epreuve=menue_epreuves()
        joueur=choisir_joueur(equipe)

        if epreuve==1:
            resultat=epreuves_maths()
            if resultat:
                cle_général+=1
                equipe[joueur]["clé_gagnées"]+=1
                print("vous avez gagner, vous avez obtenue une clé")
            else:
                print("vous avez échouer, vous n'avez pas eu de clé")
        elif epreuve==2:
            resultat=jeu_bataille_navale()
            if resultat==1:
                cle_général+=1
                equipe[joueur]["clé_gagnées"]+=1
                print("vous avez gagner, vous avez obtenue une clé")
            else:
                print("vous avez échouer, vous n'avez pas eu de clé")
        elif epreuve==3:
            resultat=epreuve_hasard()
            if resultat:
                cle_général+=1
                equipe[joueur]["clé_gagnées"]+=1
                print("vous avez gagner, vous avez obtenue une clé")
            else:
                print("vous avez échouer, vous n'avez pas eu de clé")
        elif epreuve==4:
            resultat = enigme_pere_fouras()
            if resultat:
                cle_général += 1
                equipe[joueur]["clé_gagnées"] += 1
                print("vous avez gagner, vous avez obtenue une clé")
            else:
                print("vous avez échouer, vous n'avez pas eu de clé")


    if cle_général==3:
        print(salle_de_tresor())
