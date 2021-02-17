class PitchingSeason:
    def __init__(self):
        self.id = 0
        self.teamseason = None
        self.player = None
        self.innings = 0.0
        self.era = 0.00
        self.strikeouts = 0
        self.walks = 0

    def __str__(self):
        return '|'.join([str(self.id),
                         str(self.teamseason),
                         str(self.player),
                         str(self.innings),
                         str(self.era),
                         str(self.strikeouts),
                         str(self.walks)])
