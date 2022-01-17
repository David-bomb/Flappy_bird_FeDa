from Menu import Menu
import pygame
from initial import bg, press

pygame.init()
pygame.font.init()


def start_menu(screen):
    menu = Menu()
    menu.append_option('Уровень 1', lambda: print('Уровень 1'))
    menu.append_option('Уровень 2', lambda: print('Уровень 2'))
    menu.append_option('Уровень 3', lambda: print('Уровень 3'))
    menu.append_option('Выход', lambda: quit())
    running = True
    while running:
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
