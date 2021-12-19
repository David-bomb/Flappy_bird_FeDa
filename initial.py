import pygame
import os
import sys


'''-----Функция для загрузки фото-----'''

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


'''-----Создаем все нужные спрайт-группы-----'''

sprites_lobby = pygame.sprite.Group()
sprites_games = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()

'''-----Загружаем фотографии-----'''

perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')
chet_etap = load_image('527.png')
