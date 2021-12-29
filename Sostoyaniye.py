class Sostoyaniye():
    def __init__(self):
        self.lobby = False
        self.game = False
        self.level = False

    def set(self, status):
        if status == 'Лобби':
            self.lobby = True
            self.game = False
            self.level = False
        elif status == 'Игра':
            self.lobby = False
            self.game = True
            self.level = False
        elif status == 'Уровни':
            self.lobby = False
            self.game = False
            self.level = True

    def sost(self):
        if self.lobby:
            return [True, False, False]
        elif self.game:
            return [False, True, False]
        elif self.level:
            return [False, False, True]