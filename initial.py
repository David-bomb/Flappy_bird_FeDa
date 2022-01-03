import pygame
import os
import sys
from Sostoyaniye import Sostoyaniye

def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


sprites_lobby = pygame.sprite.Group()

sprites_games = pygame.sprite.Group()
sprites_games1 = pygame.sprite.Group()
sprites_games2 = pygame.sprite.Group()

sprites_gameover = pygame.sprite.Group()
# создадим спрайт

sostoyanie = Sostoyaniye()

perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')

perv_etap = pygame.transform.scale(perv_etap, (50, 42))
vtor_etap = pygame.transform.scale(vtor_etap, (50, 42))
tret_etap = pygame.transform.scale(tret_etap, (50, 42))

tube = load_image('tube_huuuuge2.png')
tube_1 = pygame.transform.scale(tube, (500, 800))

y = 350
t = 0
g = 5
v = 0
k = 0
