import pygame
import os
import sys
from Status import Status
from random import randint

pygame.font.init()
pygame.init()
size = width, height = 450, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')


def load_image(name):  # функция подгрузки картинок
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# создание спрайтов и групп спрайтов
sprites_lobby = pygame.sprite.Group()

sprites_games = pygame.sprite.Group()
sprites_games1 = pygame.sprite.Group()
sprites_games2 = pygame.sprite.Group()

sprites_gameover = pygame.sprite.Group()
# создадим спрайт

stat = Status()  # Обьект статуса игры

# Загрузка картинок
bg = load_image('city.jpg')
bg = pygame.transform.scale(bg, (450, 500))
perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')
schet = 0
perv_etap = pygame.transform.scale(perv_etap, (50, 42))
vtor_etap = pygame.transform.scale(vtor_etap, (50, 42))
tret_etap = pygame.transform.scale(tret_etap, (50, 42))
tube = load_image('tube_huuuuge2.png')
tube_1 = pygame.transform.scale(tube, (500, 800))

# Загрузка звуков
jump = pygame.mixer.Sound("sounds/jump.ogg")
punch = pygame.mixer.Sound('sounds/punch.ogg')
tube_complete = pygame.mixer.Sound('sounds/tube_complete.ogg')
press = pygame.mixer.Sound('sounds/btn_pressed.ogg')
lose = pygame.mixer.Sound('sounds/lose.ogg')
victory = pygame.mixer.Sound('sounds/victory.ogg')

# Физические константы
y = 0
t = 0
g = 5
v = 0
k = 0
