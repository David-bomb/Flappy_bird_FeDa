class Sostoyaniye():
    def __init__(self):
        self.lobby = False
        self.game = False
        self.settings = False

    def set(self, status):
        if status == 'Лобби':
            self.lobby = True
            self.game = False
            self.settings = False
        if status == 'Настройки':
            self.lobby = False
            self.game = False
            self.settings = True
        if status == 'Игра':
            self.lobby = False
            self.game = True
            self.settings = False

    def __str__(self):
        return self.lobby, self.game, self.settings
