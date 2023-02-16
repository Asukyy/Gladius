import pygame

# Initialisation de Pygame
pygame.init()

# Création d'une fenêtre de jeu
screen = pygame.display.set_mode((400, 400))

# Définition de la couleur rouge
red = (255, 0, 0)

# Création d'un carré rouge dans la fenêtre de jeu
rect = pygame.Rect(100, 100, 50, 50)
pygame.draw.rect(screen, red, rect)

# Rafraîchissement de la fenêtre de jeu
pygame.display.flip()

# Boucle principale de jeu
running = True
while running:
    # Gestion des événements de la fenêtre de jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Fermeture de Pygame
pygame.quit()