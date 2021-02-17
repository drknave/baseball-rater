class Team:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    def __str__(self):
        return '|'.join([str(self.id),
                         self.name,
                         self.code])
