import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.menu_music = os.path.join("sounds", "game_music.mp3")
        self.game_music = os.path.join("sounds", "game_music.mp3")
        """self.game_over_music = os.path.join("sounds", "game_over_music.mp3")
        self.yellow_coin_sound = os.path.join("sounds", "yellow_coin_sound.wav")
        self.blue_coin_sound = os.path.join("sounds", "blue_coin_sound.wav")
        self.blue_obstacle_break_sound = os.path.join("sounds", "blue_obstacle_break_sound.wav")
        self.game_over_sound = os.path.join("sounds", "game_over_sound.wav")"""

        pygame.mixer.music.load(self.menu_music)
        pygame.mixer.music.set_volume(0.5)

        """self.yellow_coin_effect = pygame.mixer.Sound(self.yellow_coin_sound)
        self.blue_coin_effect = pygame.mixer.Sound(self.blue_coin_sound)
        self.blue_obstacle_break_effect = pygame.mixer.Sound(self.blue_obstacle_break_sound)
        self.game_over_effect = pygame.mixer.Sound(self.game_over_sound)
"""
    def play_menu_music(self):
        pygame.mixer.music.load(self.menu_music)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()





    def play_game_music(self):
        pygame.mixer.music.load(self.game_music)
        pygame.mixer.music.play(-1)
"""
    def play_game_over_music(self):
        pygame.mixer.music.load(self.game_over_music)
        pygame.mixer.music.play()

    def play_yellow_coin_sound(self):
        self.yellow_coin_effect.play()

    def play_blue_coin_sound(self):
        self.blue_coin_effect.play()

    def play_blue_obstacle_break_sound(self):
        self.blue_obstacle_break_effect.play()

    def play_game_over_sound(self):
        self.game_over_effect.play()
"""



# Exemple d'utilisation:
# sound_manager = SoundManager()
# sound_manager.play_menu_music()
# sound_manager.play_yellow_coin_sound()
# sound_manager.play_game_over_sound()
