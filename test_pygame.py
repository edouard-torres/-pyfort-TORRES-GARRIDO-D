
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

# Boucle principale
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérer les touches pressées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    # Dessiner
    screen.fill((0, 0, 0))  # Effacer l'écran (noir)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)  # Cercle rouge
    pygame.display.flip()  # Mettre à jour l'affichage

# Quitter
pygame.quit()
