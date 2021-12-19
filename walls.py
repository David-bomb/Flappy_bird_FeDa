import pygame
from initial import sprites_games, tube_1


class Walls(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(sprites_games)
        self.image = tube_1
        self.rect = self.image.get_rect()
        self.y = y
        self.x = 800

    def render(self, x):
        self.rect.y = self.y
        self.rect.x = x
