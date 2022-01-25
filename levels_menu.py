from Menu import Menu
import pygame
from initial import bg, press
import level_function
import game

pygame.init()
pygame.font.init()


def start_menu(screen):
    # Инициализация меню
    menu = Menu()
    menu.append_option('Уровень 1', lambda: level_function.uroven1(1))
    menu.append_option('Уровень 2', lambda: level_function.uroven1(2))
    menu.append_option('Уровень 3', lambda: level_function.uroven1(3))
    menu.append_option('Назад', lambda: game.run_game(screen))
    running = True
    while running:  # Создание биндов для использования меню
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    menu.switch(1)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    menu.switch(-1)
                if event.key == pygame.K_SPACE:
                    press.play()
                    menu.select()
            if event.type == pygame.QUIT:
                quit()
        screen.blit(bg, (0, 0))
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
