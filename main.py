import pygame

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)

# Définition de la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Création de la fenêtre
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Chargement des images pour les différentes directions
# Nous supposons que le sprite sheet est une grille 4x3 de sprites de 32x32 pixels chacun.
# Les images sont stockées dans un dictionnaire pour une référence facile.
images = {
    "bas": [pygame.image.load("images/pers-down.png").subsurface((i * 32, 0, 32, 32)) for i in range(4)],
    "haut": [pygame.image.load("images/pers-up.png").subsurface((i * 32, 0, 32, 32)) for i in range(4)],
    "gauche": [pygame.image.load("images/pers-gauche.png").subsurface((i * 32, 0, 32, 32)) for i in range(4)],
    "droite": [pygame.image.load("images/pers-droite.png").subsurface((i * 32, 0, 32, 32)) for i in range(4)]
}

# Définition du personnage
class Personnage(pygame.sprite.Sprite):

    def __init__(self, x, y, images):
        super().__init__()

        self.images = images
        self.image_index = 0
        self.direction = "bas"

        self.image = self.images[self.direction][self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):

        # Gestion des touches appuyées
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction = "gauche"
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "droite"
            self.rect.x += 5
        elif keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction = "haut"
            self.rect.y -= 5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "bas"
            self.rect.y += 5

        # Mise à jour de l'animation
        self.image_index += 1
        if self.image_index >= len(self.images[self.direction]):
            self.image_index = 0

        self.image = self.images[self.direction][self.image_index]

# Création du personnage
personnage = Personnage(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, images)

# Boucle principale du jeu
running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches appuyées
    keys = pygame.key.get_pressed()

    # Mise à jour du personnage
    personnage.update(keys)

    # Dessin du personnage
    screen.fill(BLACK)
    screen.blit(personnage.image, personnage.rect)

    # Mise à jour de l'affichage
    pygame.display.update()

# Fermeture de Pygame
pygame.quit()
