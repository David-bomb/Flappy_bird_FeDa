import pygame
from initial import comic_sans_font


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

    def draw(self, place, x, y, padding):
        for i, opt in enumerate(self.strings):
            opt_rect = opt.get_rect()
            opt_rect.topleft = (x, y + i * padding)
            if i == self.selected:
                pygame.draw.rect(place, (100, 100, 100), opt_rect)
            place.blit(opt, opt_rect)
