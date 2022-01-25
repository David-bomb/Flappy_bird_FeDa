from Status import Status
import pygame
from random import randint
from walls import Walls
from Menu import Menu
from Game_Over import game_over
from initial import sprites_games, sprites_games1, stat, sprites_gameover, t, bg, load_image, \
    jump, punch, tube_complete, press, lose
from Menu import comic_sans_font
from levels_menu import start_menu

'''----------Основной игровой цикл----------'''


def start_screen(screen):  # функция создания заставки
    intro_text = ["Доведи птицу до ее офиса", "",
                  "Но помни, что она",
                  "Должна миновать небоскребы!",
                  "Space - прыжок/действие",
                  "w - подняться на 1 в меню",
                  "s - спуститься на 1 в меню",
                  "НАЖМИТЕ ЛЮБУЮ КНОПКУ"]

    image = load_image('city.jpg')
    bg = pygame.transform.scale(image, (450, 500))
    screen.blit(bg, (0, 0))
    text_coord = 50
    for line in intro_text:
        string_rendered = comic_sans_font.render(line, 1, pygame.Color('#ffef14'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def run_game(screen):  # Функция запуска игры
    # Инициализация меню и стартовых обьектов
    sprites_games1.empty()
    y1 = randint(-302, 3)
    wall1 = Walls(y1, 250)
    pygame.font.init()
    pygame.font.init()
    menu = Menu()
    menu.append_option('Аркада', lambda: stat.set('Игра'))
    menu.append_option('Уровни', lambda: start_menu(screen))
    menu.append_option('Выйти', lambda: quit())
    global g, v, y
    clock = pygame.time.Clock()
    running = True
    fall = True
    stat.set('Лобби')
    while running:
        status = stat.sost()
        for event in pygame.event.get():
            #  Бинд кнопок
            if event.type == pygame.QUIT:  # Выход
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and status[1]:  # Прыжок
                jump.play()
                fall = False
                g = 10
                v = 10
            elif event.type == pygame.KEYDOWN and status[2]:  # Выход из окна game_over
                stat.set('Лобби')
                sprites_games1.empty()
                wall1 = Walls(randint(-302, 3), 250)
                game_over.pos()
            elif event.type == pygame.KEYDOWN and status[0]:  # Переключение между пунктами меню
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    menu.switch(1)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    menu.switch(-1)
                if event.key == pygame.K_SPACE:
                    press.play()
                    menu.select()
                    y = 1
                    g = 5
                    v = 0
                    count = 0
        if status[0]:  # Прорисовка статистики рекорд-последний результат
            screen.blit(bg, (0, 0))
            menu.draw(screen, 100, 100, 75)
            f = open("рекорд.txt", mode="r")
            text = f.readlines()
            score = str(text[0]).replace('\n', '')
            record = str(text[1])
            f.close()
            score = comic_sans_font.render(f"Последний результат: {score}", False, (255, 255, 0))
            record = comic_sans_font.render(f"Рекорд: {record}", False, (255, 255, 0))
            screen.blit(score, (75, 400))
            screen.blit(record, (150, 450))
            pygame.display.flip()
        elif status[1]:
            # Реализация физики прыжков
            if fall:
                y += g
                g += 0.1
            elif t >= 0:
                v -= 0.9
                y -= v
            else:
                fall = True
            # Прорисовка счета во время аркады
            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            sprites_games.draw(screen)
            sprites_games.update(y)
            sprites_games1.draw(screen)
            sprites_games1.update()
            text2 = comic_sans_font.render(f"SCORE: {count}", False, (255, 255, 255))
            screen.blit(text2, (20, 20))
            # Реализация стен
            if wall1.walls():
                sprites_games1.empty()
                wall1 = Walls(randint(-302, 3), 250)
            if wall1.coord()[0] == -100:
                count += 1
                tube_complete.play()
                f = open("рекорд.txt", mode="r")
                record = str(f.readlines()[1]).replace("b' ", '').replace("'", '')
                f.seek(0)
                f.close()
                f = open("рекорд.txt", mode="w")
                f.write(str(count) + '\n', )
                if int(record) < count:
                    f.write(str(count))
                else:
                    f.write(str(record))
                f.close()
            if y < 0 or y >= 495:  # Барьеры сверху и снизу
                stat.set('Уровни')
                punch.play()
                lose.play()
        elif status[2]:  # Окно Game Over
            screen.fill((0, 0, 0))
            sprites_gameover.draw(screen)
            sprites_gameover.update()
            any_button = comic_sans_font.render(f"Press any key", False, (255, 255, 0))
            screen.blit(any_button, (125, 450))
        pygame.display.flip()
        clock.tick(60)
