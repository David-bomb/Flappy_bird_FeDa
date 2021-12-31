import pygame
from initial import sprites_lobby

class Main_manu(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__(sprites_lobby)
