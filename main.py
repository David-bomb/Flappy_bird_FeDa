import pygame
from Sostoyaniye import Sostoyaniye
from initial import sprites_games, y, sprites_games1
from initial import perv_etap, vtor_etap, tret_etap, chet_etap
from walls import Walls
from Bird import bird
from random import randint





'''----------Создаем холст----------'''

pygame.init()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()


'''----------Создаем все нужные переменные и задаем все классы----------'''
y2 = 50
x1 = 550
for i in range(15):
    y1 = randint(y2 - 100, y2 + 100)
    y2 = y1
    Walls(y1 - 50, x1)
    x1 += 150
t = 0
g = 9.8
v = 0
k = 0
vniz = True
sostoyanie = Sostoyaniye()
sostoyanie.set('Игра')
'''----------Основной игровой цикл----------'''
while running:
    status = [False, True, False]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event. key == pygame.K_SPACE and status[1]:
            vniz = False
            t = 0.55
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
        sprites_games1.draw(screen)
        sprites_games1.update()
    '''-----Блок с настройками-----'''
    if status[2]:
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()