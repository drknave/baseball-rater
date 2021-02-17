class BattingSeason:
    def __init__(self):
        self.id = 0
        self.teamseason = None
        self.player = None
        self.games = 0
        self.atbats = 0
        self.hits = 0
        self.doubles = 0
        self.triples = 0
        self.homeruns = 0
        self.strikeouts = 0
        self.walks = 0
        self.steals = 0

    def __str__(self):
        return '|'.join([str(self.id), 
                         str(self.teamseason),
                         str(self.player),
                         str(self.games), 
                         str(self.atbats),
                         str(self.hits),
                         str(self.doubles),
                         str(self.triples),
                         str(self.homeruns),
                         str(self.strikeouts),
                         str(self.walks),
                         str(self.steals)])

    