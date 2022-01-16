import pygame

pygame.font.init()
comic_sans_font = pygame.font.SysFont('Fonts/Comic Sans MS.ttf', 40)

class Menu:  # инициализация меню
    def __init__(self):
        self.strings = []  # Список строк
        self.callbacks = []  # Список колбеков
        self.selected = 0  # Номер выбранной опции

    def append_option(self, option, callback):  # Функция добавления опции
        self.strings.append(comic_sans_font.render(option, True, 'yellow'))
        self.callbacks.append(callback)

    def switch(self, direction):  # Функция смены опции
        self.selected = max(0, min(self.selected + direction, len(self.strings)))

    def select(self):  # Выбор функции
        self.callbacks[self.selected]()
        if self.selected == 0:
            f = open("рекорд.txt", mode="r")
            record = str(f.readlines()[1]).replace("b' ", '').replace("'", '')
            f.seek(0)
            f.close()
            f = open("рекорд.txt", mode="w")
            f.write(str(0) + '\n')
            f.write(str(record))
            f.close()

    def draw(self, place, x, y, padding):  # Отрисовка меню
        for i, opt in enumerate(self.strings):
            opt_rect = opt.get_rect()
            opt_rect.topleft = (x, y + i * padding)
            if i == self.selected:
                pygame.draw.rect(place, (100, 100, 100), opt_rect)
            place.blit(opt, opt_rect)

    def __dir__(self):
        return self.callbacks
