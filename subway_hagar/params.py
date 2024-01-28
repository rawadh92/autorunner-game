import pygame
import sys
import random
import os
from player import Player
from obstacle import Obstacle, BlueObstacle
from bonus import Coin, BriseBrick

class GameParameters:
    def __init__(self):
        pygame.init()
        # Paramètres du jeu
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.menu_background = pygame.image.load(os.path.join("images", "menu_background.jpg")).convert()
        # Couleurs
        self.white = (255, 255, 255)

        # Groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        self.obstacles_group = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()

        # Ajout du joueur au groupe de sprites
        self.player = Player(self.all_sprites)
        self.all_sprites.add(self.player)

        # Variables pour le score et les statistiques
        self.score = 0
        self.yellow_coins_collected = 0
        self.blue_coins_collected = 0
        self.blue_obstacles_destroyed = 0
        self.blue_coins_owned = 0  # Nombre de pièces bleues que le joueur possède
        self.font = pygame.font.Font(None, 36)

    def create_obstacle(self):
        obstacle = Obstacle()
        self.all_sprites.add(obstacle)
        self.obstacles_group.add(obstacle)

    def create_blue_obstacle(self):
        blue_obstacle = BlueObstacle()
        self.all_sprites.add(blue_obstacle)
        self.obstacles_group.add(blue_obstacle)

    def create_coin(self):
        coin = Coin()
        self.all_sprites.add(coin)
        self.coins_group.add(coin)

    def create_brise_brick(self):
        brise_brick = BriseBrick()
        self.all_sprites.add(brise_brick)
        self.coins_group.add(brise_brick)

    def start_game(self):
        pygame.init()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Mise à jour des sprites
            self.all_sprites.update()

            # Gestion des collisions avec les obstacles
            obstacles_collected = pygame.sprite.spritecollide(self.player, self.obstacles_group, False)
            for obstacle in obstacles_collected:
                if isinstance(obstacle, BlueObstacle):
                    if self.blue_coins_owned > 0:
                        obstacle.reset()
                        self.blue_obstacles_destroyed += 1
                        self.score += 10
                        self.blue_coins_owned -= 1
                    else:
                        print("Game Over!")
                        pygame.quit()
                        sys.exit()
                else:
                    print("Game Over!")
                    pygame.quit()
                    sys.exit()

            # Gestion des collisions avec les pièces
            coins_collected = pygame.sprite.spritecollide(self.player, self.coins_group, True)
            for coin in coins_collected:
                if isinstance(coin, Coin):
                    self.yellow_coins_collected += 1
                    self.score += 10
                elif isinstance(coin, BriseBrick):
                    self.blue_coins_collected += 1
                    self.score += 100
                    self.blue_coins_owned += 1

            # Création d'obstacles
            if random.randint(0, 100) < 2:
                self.create_obstacle()

            # Création d'obstacles bleus
            if random.randint(0, 100) < 1:
                self.create_blue_obstacle()

            # Création de pièces
            if random.randint(0, 500) < 8:
                self.create_coin()

            # Création de pièces brise brick
            if random.randint(0, 500) < 2:
                self.create_brise_brick()

            # Augmentation de la difficulté
            if pygame.time.get_ticks() % 10000 == 0:
                for obstacle in self.obstacles_group:
                    obstacle.speed += 3

            # Dessin
            self.screen.fill(self.white)
            self.all_sprites.draw(self.screen)

            # Affichage des statistiques en haut à droite
            score_text = self.font.render("Score: {}".format(self.score), True, (0, 0, 0))
            yellow_coins_text = self.font.render("Yellow Coins: {}".format(self.yellow_coins_collected), True, (0, 0, 0))
            blue_coins_text = self.font.render("Blue Coins: {}".format(self.blue_coins_collected), True, (0, 0, 0))
            blue_obstacles_text = self.font.render("Obstacles Destroyed: {}".format(self.blue_obstacles_destroyed), True, (0, 0, 0))
            blue_coins_owned_text = self.font.render("Blue Coins Owned: {}".format(self.blue_coins_owned), True, (0, 0, 0))

            self.screen.blit(score_text, (self.width - 150, 20))
            self.screen.blit(yellow_coins_text, (self.width - 220, 60))
            self.screen.blit(blue_coins_text, (self.width - 200, 100))
            self.screen.blit(blue_obstacles_text, (self.width - 270, 140))
            self.screen.blit(blue_coins_owned_text, (self.width - 250, 180))

            pygame.display.flip()
            self.clock.tick(self.FPS)
            
            
    def show_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(self.menu_background, (0, 0))
            font = pygame.font.Font(None, 36)
            


            title_text = font.render("Subway hagar", True, (255, 255, 255))
            self.screen.blit(title_text, (self.width/2 - title_text.get_width()/2, 50))

            play_text = font.render("Jouer", True, (255, 255, 255))
            play_rect = play_text.get_rect(center=(self.width/2, 150))
            self.screen.blit(play_text, play_rect)

            settings_text = font.render("Paramètres", True, (255, 255, 255))
            settings_rect = settings_text.get_rect(center=(self.width/2, 200))
            self.screen.blit(settings_text, settings_rect)

            quit_text = font.render("Quitter", True, (255, 0, 0))
            quit_rect = quit_text.get_rect(center=(self.width/2, 250))
            self.screen.blit(quit_text, quit_rect)

            mx, my = pygame.mouse.get_pos()

            if play_rect.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.start_game()
            # Faire la logique pour afficher l'écran des paramètres
            '''if settings_rect.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.show_settings()'''

            if quit_rect.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()            
    
    
    def show_game_over_screen(self, final_score):
        game_over = True

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Afficher l'écran de game over
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)

            game_over_text = font.render("Game Over", True, (255, 0, 0))
            self.screen.blit(game_over_text, (self.width/2 - game_over_text.get_width()/2, 50))
            # Faire la logique pour afficher le meilleur score 
            score_text = font.render("Score: {}".format(final_score), True, (255, 255, 255))
            self.screen.blit(score_text, (self.width/2 - score_text.get_width()/2, 150))

            recap_text = font.render("Récapitulatif", True, (255, 255, 255))
            self.screen.blit(recap_text, (self.width/2 - recap_text.get_width()/2, 200))

            # Mettre info pour afficher le récapitulatif ici
            # ...

            restart_text = font.render("Rejouer", True, (0, 255, 0))
            restart_rect = restart_text.get_rect(center=(self.width/2 - 50, 300))
            self.screen.blit(restart_text, restart_rect)

            quit_text = font.render("Quitter", True, (255, 0, 0))
            quit_rect = quit_text.get_rect(center=(self.width/2 + 50, 300))
            self.screen.blit(quit_text, quit_rect)

            mx, my = pygame.mouse.get_pos()

            if restart_rect.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0] == 1:
                    # Réinitialiser le jeu
                    self.reset_game()
                    game_over = False

            if quit_rect.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def reset_game(self):
        # Logique pour réinitialiser le jeu (réinitialiser le score, la position du joueur, etc.)
        pass
           
    
