import pygame
import random
import os
import sys

'''----------Создаем функцию для закачки фото-----------'''
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


'''----------Создаем холст----------'''
pygame.init()
size = width, height = 600, 750
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy bird')
running = True
clock = pygame.time.Clock()
image = load_image("square.png")
perv_etap = load_image('vtor_etav.png')
vtor_etap = load_image('tret_etav.png')

t = 0
g = 9.8
y = 350
v = 0
vniz = True
k = 0

'''----------Основной игровой цикл----------'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vniz = False
            t = 0.7
    if vniz:
        y += g * t
        v = g * t
        t += 2/60
    else:
        if t >= 0:
            y -= g * t
            v -= g * 2/60
            t -= 2 / 60
        else:
            vniz = True
    if str(k).isdigit() and k & 60 == 0:
        last_image = perv_etap
    elif str(k).isdigit() and k & 4 == 15:
        last_image = vtor_etap
    k += 1
    screen.fill((230, 230, 230))
    screen.blit(image, (230, y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
