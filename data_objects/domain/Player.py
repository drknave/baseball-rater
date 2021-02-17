class Player:
    def __init__(self):
        self.id = 0
        self.brefid = ''
        self.name = ''
        self.position = ''
        
    def __str__(self):
        return '|'.join([str(self.id),
                         self.brefid,
                         self.name,
                         self.position])