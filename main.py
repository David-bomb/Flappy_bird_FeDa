import pygame
from Game_Over import Game_over, game_over
from Sostoyaniye import Sostoyaniye
from initial import sprites_games, y, sprites_games1, sostoyanie, sprites_gameover
from walls import Walls
from random import randint
from borders import Border
import time

def randint1(a, b):
    x = randint(a, b)
    if x >= -600:
        x = -600
    elif x <= -922:
        x = -922
    return x

'''----------Создаем холст----------'''

pygame.init()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()

'''----------Создаем все нужные переменные и задаем все классы----------'''

x1 = 550
test_level = []
y1 = randint(-192, 130) - 730
y2 = randint1(y1 - 100, y1 + 100)
y3 = randint1(y2 - 100, y2 + 100)
y4 = randint1(y3 - 100, y3 + 100)
y5 = randint1(y4 - 100, y4 + 100)

perv_stena = Walls(y1, 800)
vtor_stena = Walls(y2, 1050)
tret_stena = Walls(y3, 1300)
chet_stena = Walls(y4, 1550)
pyat_stena = Walls(y5, 1800)

t = 0
g = 9.8
v = 0
k = 0
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
            t = 0.55
    '''-----Блок с лобби-----'''
    if status[0]:
        screen.fill((255, 255, 255))
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


        if perv_stena.walls():
            coord_perv = perv_stena.coord()
            coord_vtor = vtor_stena.coord()
            coord_tret = tret_stena.coord()
            coord_chet = chet_stena.coord()
            coord_pyat = pyat_stena.coord()

            sprites_games1.remove(perv_stena)
            sprites_games1.remove(vtor_stena)
            sprites_games1.remove(tret_stena)
            sprites_games1.remove(chet_stena)
            sprites_games1.remove(pyat_stena)

            perv_stena = Walls(coord_vtor[1], coord_vtor[0])
            vtor_stena = Walls(coord_tret[1], coord_tret[0])
            tret_stena = Walls(coord_chet[1], coord_chet[0])
            chet_stena = Walls(coord_pyat[1], coord_pyat[0])
            igirik = randint1(coord_pyat[1] - 100, coord_pyat[1] + 100)
            pyat_stena = Walls(igirik, coord_pyat[0] + 250)

    '''-----Блок с настройками-----'''
    if status[2]:
        screen.fill((0, 0, 0))
        sprites_gameover.draw(screen)
        sprites_gameover.update()
        if not game_over.puk():
            time.sleep(1)
            sostoyanie.set('Лобби')
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
