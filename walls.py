import pygame
from initial import sprites_games, tube_1, sprites_games1
from Bird import bird
from borders import Border

left_border = Border(0, 0, 10, 500)


class Walls(pygame.sprite.Sprite):
    def __init__(self, y, x):
        # Инициализация обьектов и необходимых величин
        super().__init__(sprites_games1)
        self.image = tube_1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(tube_1)
        self.y = y
        self.rect.y = self.y
        self.x = x
        self.rect.x = self.x

    def update(self):
        # Реализация столкновений
        if pygame.sprite.collide_mask(self, bird):
            self.x = -200
        elif self.rect.colliderect(left_border):
            sprites_games1.remove(self.rect)
        else:
            self.rect.x = self.x
            if self.x > -200:
                self.x -= 2
