from initial import sprites_gameover
from initial import load_image
import pygame

image = load_image("game-over-insert-coins.gif")
image = pygame.transform.scale(image, (800, 500))


class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(sprites_gameover)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = -800
        self.b = True

    def update(self):
        if self.rect.x >= 0 and self.b:
            self.b = False
            self.rect.x = 0
        elif self.rect.x != 0:
            self.rect.x += 15

    def puk(self):
        return self.b

game_over = Game_over()