import pygame
from initial import perv_etap, vtor_etap, tret_etap
from initial import sprites_games
from initial import y
from Status import Status
from Game_Over import game_over

status = Status()


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):  # Инициализиция птицы, её положения и анимации
        super().__init__(sprites_games)
        self.image = perv_etap
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.y = y
        self.k = 0
        self.slovar = {0: perv_etap, 4: vtor_etap, 8: tret_etap}

    def update(self, y):  # Анимирование + проверка состояния
        if self.k % 12 in self.slovar:
            self.image = self.slovar[self.k % 12]
        self.k += 1
        self.rect.y = y


bird = Bird(y)
