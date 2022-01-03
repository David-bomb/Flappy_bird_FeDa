import pygame
from initial import perv_etap, vtor_etap, tret_etap
from initial import sprites_games
from initial import y
from Sostoyaniye import Sostoyaniye
from Game_Over import game_over
sostoyanie = Sostoyaniye()


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__(sprites_games)
        self.image = perv_etap
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.y = y
        self.k = 0
        self.slovar = {0: perv_etap, 4: vtor_etap, 8: tret_etap}

    def update(self, y):
        if self.k % 12 in self.slovar:
            self.image = self.slovar[self.k % 12]
        if self.y == 0:
            sostoyanie.set('Уровни')
        self.k += 1
        self.rect.y = y

bird = Bird(y)