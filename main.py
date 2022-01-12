import pygame
from initial import comic_sans_font, start_screen
from random import randint
from Menu import Menu
from game import run_game


'''----------Создаем холст----------'''
pygame.init()
size = width, height = 400, 500
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
pygame.display.set_caption('Flappy bird')
# Создание меню
menu = Menu()
menu.append_option('Аркада', lambda: run_game(screen))
menu.append_option('Уровни', lambda: print('WIP'))
menu.append_option('Выйти', lambda: quit())
# Запуск заставки
run1 = True
running = True
start_screen(screen)
while run1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN or \
                event.type == pygame.MOUSEBUTTONDOWN:
            run1 = False


# Запуск меню
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
