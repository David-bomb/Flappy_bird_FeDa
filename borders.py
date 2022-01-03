import pygame
from Bird import Bird
from initial import sprites_games2


class Border(pygame.sprite.Sprite):
    def __init__(self, y, x, width, height):
        # Инициализация обьектов и необходимых величин
        super().__init__(sprites_games2)
        self.barrierRect = pygame.Rect(
            x, y, width, height)
        self.x = x
        self.y = y

    def rect(self):
        return self.barrierRect
