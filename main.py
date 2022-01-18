import pygame
from game import start_screen
from initial import screen
from random import randint
from Menu import Menu
from game import run_game
from initial import bg, press

'''----------Создаем холст---------'''
# Запуск заставки
run1 = True
while run1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN or \
                event.type == pygame.MOUSEBUTTONDOWN:
            press.play()
            run1 = False
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    start_screen(screen)
    pygame.display.flip()

run_game(screen)
