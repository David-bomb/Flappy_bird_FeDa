import pygame
from Game_Over import game_over
from initial import sprites_games, sprites_games1, sostoyanie, sprites_gameover, t, g, v, y
from walls import Walls
from random import randint
import time

'''Создаю функцию выбора рандомных к   оординат, чтоб трубы не выходили за пределы экрана'''
def randint1(a, b):
    x = randint(a, b)
    if x >= 3:
        x = 3
    elif x <= -302:
        x = -302
    return x


'''----------Создаем холст----------'''

pygame.init()
size = width, height = 400, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()

'''----------Создаем все нужные переменные и задаем все классы----------'''

'''Создаю координаты для текстур'''
y1 = randint(-302, 3)

'''Создаю четыре текстуры, чтоб они занимали весь экран'''
perv_stena = Walls(y1, 200)

vniz = True

sostoyanie.set('Игра')
'''----------Основной игровой цикл----------'''
while running:
    status = sostoyanie.sost()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and status[1]:
            vniz = False
            g = 5
            v = 10
        if event.type == pygame.MOUSEBUTTONDOWN and status[0]:
            pass
    if status[0]:
        screen.fill((255, 255,  255))
    elif status[1]:
        if vniz:
            y += g
            g += 0.1
        elif t >= 0:
            v -= 0.9
            y -= v
        else:
            vniz = True
        screen.fill((100, 100, 100))
        sprites_games.draw(screen)
        sprites_games.update(y)
        sprites_games1.draw(screen)
        sprites_games1.update()

        if perv_stena.walls():
            perv = perv_stena.coord()
            sprites_games1.remove(perv_stena)
            perv_stena = Walls(randint(-302, 3), 180)
    elif status[2]:
        screen.fill((0, 0, 0))
        sprites_gameover.draw(screen)
        sprites_gameover.update()
        if not game_over.puk():  # Когда картинка game_over целиком вылезла проходит секунда и открывается главное меню (Лобби)
            time.sleep(1)
            sostoyanie.set('Лобби')
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
