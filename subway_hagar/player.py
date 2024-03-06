import pygame
from pygame.locals import *

pygame.init()
écran = pygame.display.set_mode((640, 480))


class CadreStatique:
    """Sprite statique unique d'une feuille de sprites.

    image: surface représentant la feuille de sprites
    ligne: ligne dans la feuille de sprites où se trouve le sprite
    colonne: colonne dans la feuille de sprites où se trouve le sprite
    nrows: nombre de lignes de sprites
    ncols: nombre de colonnes de sprite
    """
    def __init__(self, image, ligne, colonne, nrows, ncols):
        self.image = image
        rect = image.get_rect()
        largeur_frame = rect.width // ncols
        hauteur_frame = rect.height // nrows
        self._xoffset = colonne * largeur_frame
        self._yoffset = ligne * hauteur_frame
        self._rect = pygame.Rect(self._xoffset, self._yoffset,
                                 largeur_frame, hauteur_frame)

    def update(self, dt):
        pass

    @property
    def rect(self):
        "Le rectangle dans la feuille de sprites délimitant le sprite désiré."
        return self._rect


class CadreAnimé(CadreStatique):
    """Sprite animé d'une feuille de sprites.

    L'animation est censée être contenue sur une ligne. Elle peut commencer à une
    colonne différente de la colonne 0, auquel cas l'animation bouclera à partir de
    la colonne de départ jusqu'au dernier sprite de colonne.

    durée: durée du frame exprimée en secondes.
    """
    def __init__(self, image, ligne, colonne, durée, nrows, ncols):
        super().__init__(image, ligne, colonne, nrows, ncols)
        self.durée = durée
        self.temps = 0
        self._largeur_frames_animés = (ncols - colonne) * self._rect.width

    def update(self, dt):
        self.temps += dt / 1000
        while self.temps > self.durée:
            self.temps -= self.durée
            gauche = self._rect.left
            étape = self._rect.width
            gauche = (gauche - self._xoffset + étape) % self._largeur_frames_animés
            self._rect.left = gauche + self._xoffset


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('C:/Users/Adame/OneDrive/Documents/GitHub/autorunner-game/subway_hagar/sprite_image/zoro.png').convert_alpha()

    def __init__(self, x, y):
        super().__init__()
        NROWS = 4#nombre de lignes de sprites a changer selon le sprite
        NCOLS = 4#nombre de colonnes de sprite
        self._frames = {
            "STATIQUE": {
                "BAS": CadreStatique(self.image, 0, 0, NROWS, NCOLS),
                "GAUCHE": CadreStatique(self.image, 1, 0, NROWS, NCOLS),
                "DROITE": CadreStatique(self.image, 2, 0, NROWS, NCOLS),
                "HAUT": CadreStatique(self.image, 3, 0, NROWS, NCOLS),
            },
            "ANIMÉ": {
                "BAS": CadreAnimé(self.image, 0, 1, 0.2, NROWS, NCOLS),
                "GAUCHE": CadreAnimé(self.image, 1, 1, 0.2, NROWS, NCOLS),
                "DROITE": CadreAnimé(self.image, 2, 1, 0.2, NROWS, NCOLS),
                "HAUT": CadreAnimé(self.image, 3, 1, 0.2, NROWS, NCOLS),
            }
        }

        self.état = "STATIQUE"
        self.orientation = "GAUCHE"
        self._frame = self._frames[self.état][self.orientation]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.rect = self.rect.inflate(-75, -75)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y), self._frame.rect)

    def updat(self, dt):
        self._frame.update(dt)
        dt_sec = dt / 1000
        self.x += self.vx * dt_sec
        self.y += self.vy * dt_sec

    def réagir(self, événements):
        for événement in événements:
            if événement.type == KEYDOWN:
                if événement.key == K_LEFT:
                    self.vx -= 70
                elif événement.key == K_RIGHT:
                    self.vx += 70
                elif événement.key == K_DOWN:
                    self.vy += 70
                elif événement.key == K_UP:
                    self.vy -= 70
                self._mettre_à_jour_frame()

            elif événement.type == KEYUP:
                if événement.key == K_LEFT:
                    self.vx += 70
                elif événement.key == K_RIGHT:
                    self.vx -= 70
                elif événement.key == K_DOWN:
                    self.vy -= 70
                elif événement.key == K_UP:
                    self.vy += 70
                self._mettre_à_jour_frame()

    def _mettre_à_jour_frame(self):
        if self.vy < 0:
            self.état = "ANIMÉ"
            self.orientation = "HAUT"
        elif self.vx < 0:
            self.état = "ANIMÉ"
            self.orientation = "GAUCHE"
        elif self.vx > 0:
            self.état = "ANIMÉ"
            self.orientation = "DROITE"
        elif self.vy > 0:
            self.état = "ANIMÉ"
            self.orientation = "BAS"
        else:
            self.état = "STATIQUE"
        self._frame = self._frames[self.état][self.orientation]
