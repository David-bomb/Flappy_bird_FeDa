from Sostoyaniye import Sostoyaniye
import pygame
from random import randint
from walls import Walls
import time
from Menu import Menu
from Game_Over import game_over
from initial import sprites_games, sprites_games1, sostoyanie, sprites_gameover, t, g, v, y, bg, load_image, screen, schet
from Menu import comic_sans_font

'''----------Основной игровой цикл----------'''


def start_screen(screen):  # функция создания заставки
    intro_text = ["Доведи птицу до ее офиса", "",
                  "Но помни, что она",
                  "Должна миновать небоскребы!",
                  "Space - прыжок/взамодействие",
                  "w - подняться на 1 в меню",
                  "s - спуститься на 1 в меню",
                  "НАЖМИТЕ ЛЮБУЮ КНОПКУ"]

    image = load_image('city.jpg')
    fon = pygame.transform.scale(image, (450, 500))
    screen.blit(fon, (0, 0))
    text_coord = 50
    for line in intro_text:
        string_rendered = comic_sans_font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

pygame.font.init()
comic_sans_font = pygame.font.SysFont('Fonts/Comic Sans MS.ttf', 40)
text2 = comic_sans_font.render("", False, (0, 0, 0))
global schet
def run_game(screen):
    pygame.font.init()
    comic_sans_font = pygame.font.SysFont('Fonts/Comic Sans MS.ttf', 40)
    menu = Menu()
    menu.append_option('Аркада', lambda: sostoyanie.set('Игра'))
    menu.append_option('Уровни', lambda: print('WIP'))
    menu.append_option('Выйти', lambda: quit())
    global g, v, y
    clock = pygame.time.Clock()
    running = True
    fall = True
    sostoyanie.set('Лобби')
    y1 = randint(-302, 3)
    perv_stena = Walls(y1, 250)
    while running:
        status = sostoyanie.sost()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and status[1]:
                fall = False
                g = 5
                v = 10
            elif event.type == pygame.KEYDOWN and status[2]:
                sostoyanie.set('Лобби')
                sprites_games1.remove(perv_stena)
                perv_stena = Walls(randint(-302, 3), 250)
                game_over.jk()
            elif event.type == pygame.KEYDOWN and status[0]:
                if event.key == pygame.K_DOWN or event.key == pygame.K_w:
                    menu.switch(1)
                if event.key == pygame.K_UP or event.key == pygame.K_s:
                    menu.switch(-1)
                if event.key == pygame.K_SPACE:
                    menu.select()
                    y = 1
                    g = 5
                    v = 0
                    schet = 0
        if status[0]:
            screen.fill((0, 0, 0))
            menu.draw(screen, 100, 100, 75)
            f = open("рекорд.txt", mode="r")
            a = f.readlines()
            sc = str(a[0]).replace('\n', '')
            rec = str(a[1])
            f.close()
            sc = comic_sans_font.render(f"Последний результат: {sc}", False, (255, 255, 0))
            rec = comic_sans_font.render(f"Рекорд: {rec}", False, (255, 255, 0))
            screen.blit(sc, (75, 400))
            screen.blit(rec, (150, 450))
            pygame.display.flip()
        elif status[1]:
            if fall:
                y += g
                g += 0.1
            elif t >= 0:
                v -= 0.9
                y -= v
            else:
                fall = True
            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            sprites_games.draw(screen)
            sprites_games.update(y)
            sprites_games1.draw(screen)
            sprites_games1.update()
            text2 = comic_sans_font.render(f"SCORE", False, (255, 255, 255))
            text3 = comic_sans_font.render(f"{schet}", False, (255, 255, 255))
            screen.blit(text2, (20, 20))
            screen.blit(text3, (20, 50))
            if perv_stena.walls():
                sprites_games1.remove(perv_stena)
                perv_stena = Walls(randint(-302, 3), 250)
            if perv_stena.coord()[0] == -100:
                schet += 1
                f = open("рекорд.txt", mode="r")
                record = str(f.readlines()[1]).replace("b' ", '').replace("'", '')
                f.seek(0)
                f.close()
                f = open("рекорд.txt", mode="w")
                f.write(str(schet) + '\n', )
                if int(record) < schet:
                    f.write(str(schet))
                else:
                    f.write(str(record))
                f.close()
            if y < 0 or y >= 495:
                sostoyanie.set('Уровни')
        elif status[2]:
            screen.fill((0, 0, 0))
            sprites_gameover.draw(screen)
            sprites_gameover.update()
        pygame.display.flip()
        clock.tick(60)