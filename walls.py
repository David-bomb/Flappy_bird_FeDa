import pygame
from initial import sprites_games, tube_1, sprites_games1, sostoyanie, punch, lose
from Bird import bird
from Sostoyaniye import Sostoyaniye

global schet


class Walls(pygame.sprite.Sprite):
    def __init__(self, y, x):
        # Инициализация обьектов и необходимых величин
        super().__init__(sprites_games1)
        self.image = tube_1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = y
        self.x = x
        self.rect.x = self.x
        self.nov = False

    def update(self):
        # Реализация столкновений
        if pygame.sprite.collide_mask(self, bird):
            punch.play()
            lose.play()
            sostoyanie.set('Уровни')
        elif self.rect.x <= -280:
            self.nov = True
        else:
            self.rect.x = self.x
            self.x -= 2

    def walls(self):  # показывает ушла ли труба за пределы экрана
        if self.nov:
            self.nov = False
            return True
        return False

    def der(self):
        self.nov = False

    def coord(self):  # выводит координаты трубы
        return [self.rect.x, self.rect.y]
