import pygame
import os
import sys
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
sprites_lobby = pygame.sprite.Group()
sprites_games = pygame.sprite.Group()
# создадим спрайт
sprite = pygame.sprite.Sprite()
perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')
chet_etap = load_image('527.png')
tube = load_image('tube_FeDa_1.png')
tube_1 = pygame.transform.scale(tube, (500, 650))