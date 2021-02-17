class TeamSeason:
    def __init__(self):
        self.id = 0
        self.team = None
        self.season = 0

    def __str__(self):
        return '|'.join([str(self.id),
                         str(self.team),
                         str(self.season)])