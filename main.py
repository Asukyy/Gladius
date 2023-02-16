import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
window = pygame.display.set_mode((800, 600))

# Boucle principale 
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
#affiche un carre vert au milieu de l'écran
    pygame.draw.rect(window, (0, 255, 0), pygame.Rect(300, 200, 200, 200))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()