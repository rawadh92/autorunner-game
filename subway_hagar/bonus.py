import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 30
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (self.size // 2, self.size // 2), self.size // 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(-600, 0)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.reset()

    def reset(self):
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(-600, 0)

class BriseBrick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 30
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (self.size // 2, self.size // 2), self.size // 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(-600, 0)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.reset()

    def reset(self):
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(-600, 0)
