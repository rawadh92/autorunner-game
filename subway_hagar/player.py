import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.size = 25
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=(400, 550))
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
