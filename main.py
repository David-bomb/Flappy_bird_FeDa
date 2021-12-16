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
perv_etap = load_image('524.png')
vtor_etap = load_image('525.png')
tret_etap = load_image('526.png')
chet_etap = load_image('527.png')

t = 0
g = 9.8
y = 350
v = 0
vniz = True
k = 0

print(perv_etap, vtor_etap)
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
    if k & 12 == 0:
        last_image = perv_etap
    elif k & 12 == 4:
        last_image = vtor_etap
    elif k & 12 == 8:
        last_image = tret_etap
    elif k & 16 == 11:
        last_image = chet_etap
    k += 1
    screen.fill((100, 100, 100))
    screen.blit(last_image, (230, y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
