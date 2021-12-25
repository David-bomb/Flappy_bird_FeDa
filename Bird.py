import pygame
from initial import perv_etap, vtor_etap, tret_etap
from initial import chet_etap, sprites_games, sprites_games1
from initial import y


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__(sprites_games)
        self.image = perv_etap
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.y = y
        self.k = 0
        self.last_image = None

    def update(self, y):
        if self.k & 12 == 0:
            self.image = perv_etap
            self.mask = pygame.mask.from_surface(self.image)
        elif self.k & 12 == 4:
            self.image = vtor_etap
            self.mask = pygame.mask.from_surface(self.image)
        elif self.k & 12 == 8:
            self.image = tret_etap
            self.mask = pygame.mask.from_surface(self.image)
        elif self.k & 16 == 11:
            self.image = chet_etap
            self.mask = pygame.mask.from_surface(self.image)
        self.k += 1
        self.rect.x = 230
        self.rect.y = y

bird = Bird(y)