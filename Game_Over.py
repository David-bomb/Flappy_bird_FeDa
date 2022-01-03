from initial import sprites_gameover
from initial import load_image
import pygame

image = load_image("gameover.jpg")
image = pygame.transform.scale(image, (400, 500))


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
        else:
            self.rect.x += 15

    def puk(self):  # Функция, которая показывает полностью выехала картинка или нет
        return self.b


game_over = Game_over()
