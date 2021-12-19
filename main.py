import pygame
import os
import sys
from Sostoyaniye import Sostoyaniye
from Bird import Bird
from initial import sprites_games


'''----------Создаем холст----------'''

pygame.init()
size = width, height = 600, 750
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()

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