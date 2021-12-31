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
size = width, height = 600, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()

'''----------Создаем все нужные переменные и задаем все классы----------'''

'''Создаю координаты для текстур'''
y1 = randint(-302, 3)
y2 = randint1(y1 - 150, y1 + 150)
y4 = randint1(y2 - 150, y2 + 150)

'''Создаю четыре текстуры, чтоб они занимали весь экран'''
perv_stena = Walls(y1, 600)
vtor_stena = Walls(y2, 850)
chet_stena = Walls(y4, 1100)

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
            t = 17
            g = 5
            v = 10

        if event.type == pygame.MOUSEBUTTONDOWN and status[0]:
            pass
    if status[0]:
        screen.fill((255, 255,  255))
    elif status[1]:
        if vniz:
            y += g
            g += 0.2
        elif t >= 0:
            v -= 1
            y -= v
            t -= 1
        else:
            vniz = True
        screen.fill((100, 100, 100))
        sprites_games.draw(screen)
        sprites_games.update(y)
        sprites_games1.draw(screen)
        sprites_games1.update()

        if perv_stena.walls():
            mas = [perv_stena, vtor_stena, chet_stena]
            mas1 = []
            for i in range(3):
                mas1.append(mas[i].coord())
                sprites_games1.remove(mas[i])

            perv_stena = Walls(mas1[1][1], mas1[1][0])
            vtor_stena = Walls(mas1[2][1], mas1[2][0])
            igirik = randint1(mas1[2][1] - 150, mas1[2][1] + 150)
            chet_stena = Walls(igirik, mas1[2][0] + 250)


    if status[2]:
        screen.fill((0, 0, 0))
        sprites_gameover.draw(screen)
        sprites_gameover.update()
        if not game_over.puk():  # Когда картинка game_over целиком вылезла проходит секунда и открывается главное меню (Лобби)
            time.sleep(1)
            sostoyanie.set('Лобби')
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
