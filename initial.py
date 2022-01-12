import pygame
import os
import sys
from Sostoyaniye import Sostoyaniye

pygame.font.init()


def load_image(name):  # функция подгрузки картинок
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


comic_sans_font = pygame.font.SysFont('Fonts/Comic Sans MS.ttf', 40)


def start_screen(screen):  # функция создания заставки
    intro_text = ["Доведи птицу до ее офиса", "",
                  "Но помни, что она",
                  "Должна миновать небоскребы!",
                  "Space - прыжок/взамодействие",
                  "w - подняться на 1 в меню",
                  "s - спуститься на 1 в меню",
                  "НАЖМИТЕ ЛЮБУЮ КОМНТАУ"]

    fon = pygame.transform.scale(load_image('city.jpg'), (400, 500))
    screen.blit(fon, (0, 0))
    text_coord = 50
    for line in intro_text:
        string_rendered = comic_sans_font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


# создание спрайтов и групп спрайтов
sprites_lobby = pygame.sprite.Group()

sprites_games = pygame.sprite.Group()
sprites_games1 = pygame.sprite.Group()
sprites_games2 = pygame.sprite.Group()

sprites_gameover = pygame.sprite.Group()
# создадим спрайт

sostoyanie = Sostoyaniye()

bg = load_image('city.jpg')
bg = pygame.transform.scale(bg, (400, 500))

perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')

perv_etap = pygame.transform.scale(perv_etap, (50, 42))
vtor_etap = pygame.transform.scale(vtor_etap, (50, 42))
tret_etap = pygame.transform.scale(tret_etap, (50, 42))

tube = load_image('tube_huuuuge2.png')
tube_1 = pygame.transform.scale(tube, (500, 800))

# Физические константы
y = 350
t = 0
g = 5
v = 0
k = 0
