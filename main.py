import pygame
from initial import comic_sans_font
from random import randint
from Menu import Menu
from game import run_game
'''Создаю функцию выбора рандомных координат, чтоб трубы не выходили за пределы экрана'''





'''----------Создаем холст----------'''

pygame.init()
size = width, height = 400, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')
running = True
menu = Menu()
menu.append_option('Play', lambda: run_game(screen))
menu.append_option('Что-то еще', lambda: print('ПАУ'))
menu.append_option('QUIT', lambda: quit())

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_s:
                    menu.switch(1)
                if i.key == pygame.K_w:
                    menu.switch(-1)
                if i.key == pygame.K_SPACE:
                    menu.select()
        screen.fill((0, 0, 0))
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
pygame.quit()
