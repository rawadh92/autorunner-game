import pygame
import sys
import random
from player import Player
from obstacle import Obstacle, BlueObstacle
from bonus import Coin, BriseBrick

pygame.init()

# Paramètres du jeu
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60

# Couleurs
white = (255, 255, 255)

# Groupe de sprites
all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()

# Ajout du joueur au groupe de sprites
player = Player(all_sprites)
all_sprites.add(player)

# Fonction pour créer un obstacle
def create_obstacle():
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles_group.add(obstacle)

# Fonction pour créer un obstacle bleu
def create_blue_obstacle():
    blue_obstacle = BlueObstacle()
    all_sprites.add(blue_obstacle)
    obstacles_group.add(blue_obstacle)

# Fonction pour créer une pièce
def create_coin():
    coin = Coin()
    all_sprites.add(coin)
    coins_group.add(coin)

# Fonction pour créer une pièce brise brick
def create_brise_brick():
    brise_brick = BriseBrick()
    all_sprites.add(brise_brick)
    coins_group.add(brise_brick)

# Variables pour le score et les statistiques
score = 0
yellow_coins_collected = 0
blue_coins_collected = 0
blue_obstacles_destroyed = 0
blue_coins_owned = 0  # Nombre de pièces bleues que le joueur possède
font = pygame.font.Font(None, 36)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour des sprites
    all_sprites.update()

    # Gestion des collisions avec les obstacles
    obstacles_collected = pygame.sprite.spritecollide(player, obstacles_group, False)
    for obstacle in obstacles_collected:
        if isinstance(obstacle, BlueObstacle):
            if blue_coins_owned > 0:
                # Si le joueur a une pièce bleue, détruire l'obstacle bleu et gagner +10 points
                obstacle.reset()
                blue_obstacles_destroyed += 1
                score += 10
                blue_coins_owned -= 1
            else:
                # Sinon, si le joueur n'a pas de pièce bleue, c'est un Game Over
                print("Game Over!")
                pygame.quit()
                sys.exit()
        else:
            # Si c'est un obstacle normal (noir), c'est un Game Over
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Gestion des collisions avec les pièces
    coins_collected = pygame.sprite.spritecollide(player, coins_group, True)
    for coin in coins_collected:
        if isinstance(coin, Coin):
            yellow_coins_collected += 1
            score += 10
        elif isinstance(coin, BriseBrick):
            blue_coins_collected += 1
            score += 100
            blue_coins_owned += 1

    # Création d'obstacles
    if random.randint(0, 100) < 3:  # Moins d'obstacles au début
        create_obstacle()

    # Création d'obstacles bleus
    if random.randint(0, 500) < 2:  # Crée un obstacle bleu avec une faible probabilité
        create_blue_obstacle()

    # Création de pièces
    if random.randint(0, 500) < 2:  # Crée une pièce avec une faible probabilité
        create_coin()

    # Création de pièces brise brick
    if random.randint(0, 500) < 2:  # Crée une pièce brise brick avec une faible probabilité
        create_brise_brick()

    # Augmentation de la difficulté
    if pygame.time.get_ticks() % 30000 == 0:  # Augmente la difficulté toutes les 30 secondes
        for obstacle in obstacles_group:
            obstacle.speed += 1

    # Dessin
    screen.fill(white)
    all_sprites.draw(screen)

    # Affichage des statistiques en haut à droite
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    yellow_coins_text = font.render("Yellow Coins: {}".format(yellow_coins_collected), True, (0, 0, 0))
    blue_coins_text = font.render("Blue Coins: {}".format(blue_coins_collected), True, (0, 0, 0))
    blue_obstacles_text = font.render("Blue Obstacles Destroyed: {}".format(blue_obstacles_destroyed), True, (0, 0, 0))
    blue_coins_owned_text = font.render("Blue Coins Owned: {}".format(blue_coins_owned), True, (0, 0, 0))

    screen.blit(score_text, (width - 150, 20))
    screen.blit(yellow_coins_text, (width - 220, 60))
    screen.blit(blue_coins_text, (width - 200, 100))
    screen.blit(blue_obstacles_text, (width - 270, 140))
    screen.blit(blue_coins_owned_text, (width - 250, 180))

    pygame.display.flip()
    clock.tick(FPS)
