
import pygame

# Initialisation
pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Jeu avec Pygame")

# Variables
x, y = 400, 300  # Position initiale du cercle
radius = 30      # Rayon du cercle
speed = 5        # Vitesse de déplacement
running = True
pygame.display.set_caption("Détection de clic sur un rectangle")


def grille(screen,indice):
    x, y = 400, 300
    for i in range(3):
        x= 400
        y+=20
        for j in range(3):
            if indice[0] == i and indice[1] == j:
                pygame.draw.rect(screen, (255,0,0), (x,y,100,100))
            else:
                pygame.draw.rect(screen, (0,255,0), (x,y,100,100))

            x+=120
        y+=120





# Initialisation
pygame.init()
pygame.display.set_caption("Détection de clic sur un rectangle")
clock = pygame.time.Clock()

# Définition du rectangle
rect1 = pygame.Rect(400, 320, 100, 100)  # (x, y, largeur, hauteur)
rect2 = pygame.Rect(520, 320, 100, 100)  # (x, y, largeur, hauteur)
rect3 = pygame.Rect(640, 320, 100, 100)  # (x, y, largeur, hauteur)
rect4 = pygame.Rect(400, 460, 100, 100)  # (x, y, largeur, hauteur)
rect5 = pygame.Rect(520, 460, 100, 100)  # (x, y, largeur, hauteur)
rect6 = pygame.Rect(640, 460, 100, 100)  # (x, y, largeur, hauteur)
rect7 = pygame.Rect(400, 600, 100, 100)  # (x, y, largeur, hauteur)
rect8 = pygame.Rect(520, 600, 100, 100)  # (x, y, largeur, hauteur)
rect9 = pygame.Rect(640, 600, 100, 100)  # (x, y, largeur, hauteur)


rect_color = (0, 255, 0)  # Couleur normale du rectangle
clicked_color = (255, 0, 0)  # Couleur lorsqu'il est cliqué

rectangle={"rect1":[rect1,0,0],"rect2":[rect2,0,1],"rect3":[rect3,0,2],"rect4":[rect4,1,0],"rect5":[rect5,1,1],"rect6":[rect6,1,2],"rect7":[rect7,2,0],"rect8":[rect8,2,1],"rect9":[rect9,2,2] }





running = True
while running:
    indice=[-1,-1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Détection de clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Bouton gauche de la souris
            mouse_pos = pygame.mouse.get_pos()  # Position de la souris
            for i in rectangle:
                if rectangle[i][0].collidepoint(mouse_pos):  # Vérifie si la souris est sur le rectangle
                    indice=[rectangle[i][1],rectangle[i][2]]
                    print("Rectangle cliqué !",indice)



    # Dessin
    screen.fill((30, 30, 30))  # Fond de la fenêtre
    grille(screen,indice)
    #pygame.draw.rect(screen, rect_color, rect)


    # Mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60)

pygame.quit()




