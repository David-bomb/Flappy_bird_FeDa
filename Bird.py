import pygame
from initial import perv_etap, vtor_etap, tret_etap, chet_etap, sprites_games


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        global perv_etap
        super().__init__(sprites_games)
        self.image = perv_etap
        self.rect = self.image.get_rect()
        self.y = y
        self.k = 0
        self.last_image = None

    def update(self, y):
        if self.k & 12 == 0:
            self.image = perv_etap
        elif self.k & 12 == 4:
            self.image = vtor_etap
        elif self.k & 12 == 8:
            self.image = tret_etap
        elif self.k & 16 == 11:
            self.image = chet_etap
        self.k += 1
        self.rect.x = 230
        self.rect.y = y