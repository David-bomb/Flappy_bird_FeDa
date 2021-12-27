import pygame
from initial import sprites_games2


class Border(pygame.sprite.Sprite):
    def __init__(self, y, x):
        # Инициализация обьектов и необходимых величин
        super().__init__(sprites_games2)
