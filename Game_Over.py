from initial import sprites_gameover
from initial import load_image
import pygame

image = load_image("gameover.jpg")
image = pygame.transform.scale(image, (450, 500))
image_victory = load_image("victory.png")
image_victory = pygame.transform.scale(image_victory, (450, 500))


class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(sprites_gameover)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = -800
        self.b = True

    def update(self, victory=0):
        if victory == 100:
            self.image = image_victory
            if self.rect.x >= 0 and self.b:
                self.b = False
                self.rect.x = 0
            elif not self.b:
                self.rect.x = 0
            else:
                self.rect.x += 15
        else:
            self.image = image
            if self.rect.x >= 0 and self.b:
                self.b = False
                self.rect.x = 0
            elif not self.b:
                self.rect.x = 0
            else:
                self.rect.x += 15

    def gameover_check(self):  # Функция, которая показывает полностью выехала картинка или нет
        return self.b

    def pos(self):
        self.rect.x = -800


game_over = Game_over()
