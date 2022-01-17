from Sostoyaniye import Sostoyaniye
import pygame
from random import randint
from walls import Walls
from Menu import Menu
from Game_Over import game_over
import game
from initial import sprites_games, sprites_games1, sostoyanie, sprites_gameover, t, bg, load_image, jump, punch, \
    tube_complete, press, lose, v, y, g, screen
from Menu import comic_sans_font


def uroven1(levelok):
    running1 = True
    fall1 = True
    global v, y, g
    y = 0
    clock1 = pygame.time.Clock()
    sprites_games1.empty()
    perv_stena = Walls(-100, 250)
    perv_stena.der()
    sostoyanie.set('Игра')
    schet1 = 0
    uroven = {1: "levels/level1.txt", 2: "levels/level2.txt", 3: "levels/level3.txt"}
    f = open(f"{uroven[int(levelok)]}", mode="r")
    kolvo = len(f.readlines())
    f.close()
    precent = 0
    while running1:
        status = sostoyanie.sost()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and status[1]:
                fall1 = False
                g = 5
                v = 10
            elif event.type == pygame.KEYDOWN and not event.key == pygame.K_SPACE and status[2]:
                sprites_games1.empty()
                perv_stena = Walls(randint(-302, 3), 250)
                game_over.pos()
                game.run_game(screen)
        if status[1]:
            if fall1:
                y += g
                g += 0.1
            elif t >= 0:
                v -= 0.9
                y -= v
            else:
                fall1 = True
            f = open(f"{uroven[int(levelok)]}", mode="r")
            coord_y_level = int(f.readlines()[schet1].replace('\n', ''))
            f.close()
            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            sprites_games.draw(screen)
            sprites_games.update(y)
            sprites_games1.draw(screen)
            sprites_games1.update()
            text2 = comic_sans_font.render(f"COMPLETED", False, (255, 255, 255))
            text3 = comic_sans_font.render(f"{precent}%", False, (255, 255, 255))
            screen.blit(text2, (20, 20))
            screen.blit(text3, (20, 50))
            if perv_stena.walls():
                sprites_games1.empty()
                perv_stena = Walls(coord_y_level, 250)
                if schet1 == kolvo - 1:
                    precent = 100
                if schet1 < kolvo - 1:
                    schet1 += 1
                    precent = schet1 / kolvo * 100 // 1
            if precent == 100:
                sostoyanie.set('Уровни')
            if y < 0 or y >= 495:
                sostoyanie.set('Уровни')
        elif status[2]:
            if precent == 100:
                screen.fill((0, 0, 0))
                sprites_gameover.draw(screen)
                sprites_gameover.update(100)
                any_button = comic_sans_font.render(f"Press any key", False, (255, 255, 0))
                screen.blit(any_button, (125, 450))
            else:
                screen.fill((0, 0, 0))
                sprites_gameover.draw(screen)
                sprites_gameover.update(1)
                any_button = comic_sans_font.render(f"Press any key", False, (255, 255, 0))
                screen.blit(any_button, (125, 450))
        pygame.display.flip()
        clock1.tick(60)