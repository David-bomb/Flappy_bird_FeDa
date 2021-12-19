import pygame
import os
import sys
from Sostoyaniye import Sostoyaniye

'''----------Создаем функцию для закачки фото-----------'''


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


'''----------Создаем холст----------'''

pygame.init()
size = width, height = 600, 750
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()
sprites_lobby = pygame.sprite.Group()
sprites_games = pygame.sprite.Group()
# создадим спрайт
sprite = pygame.sprite.Sprite()
perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')
chet_etap = load_image('527.png')


'''----------Создаем класс с птицей----------'''


class Bird(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__(sprites_games)
        self.image = perv_etap
        self.rect = self.image.get_rect()
        self.y = y
        self.k = 0
        self.last_image = None

    def update(self, y):
        if self.k & 12 == 0:
            self.image = perv_etap
        elif self.k & 12 == 4:
            self.image = vtor_etap
        elif self.k & 12 == 8:
            self.image = tret_etap
        elif self.k & 16 == 11:
            self.image = chet_etap
        self.k += 1
        self.rect.x = 230
        self.rect.y = y


'''----------Создаем все нужные переменные и задаем все классы----------'''

t = 0
g = 9.8
y = 350
v = 0
k = 0

vniz = True

sostoyanie = Sostoyaniye()
sostoyanie.set('Игра')
Bird(y)


'''----------Основной игровой цикл----------'''
while running:
    status = [False, True, False]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and status[1]:
            vniz = False
            t = 0.7
    '''-----Блок с лобби-----'''
    if status[0]:
        pass
    '''-----Блок с игрой-----'''
    if status[1]:
        if vniz:
            y += g * t
            v = g * t
            t += 2 / 60
        elif t >= 0:
            y -= g * t
            v -= g * 2 / 60
            t -= 2 / 60
        else:
            vniz = True
        screen.fill((100, 100, 100))
        sprites_games.draw(screen)
        sprites_games.update(y)
    '''-----Блок с настройками-----'''
    if status[2]:
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
