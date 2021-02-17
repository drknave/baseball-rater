class PlayerSchema:
    def __init__(self):
        self.id = 0
        self.brefid = ''
        self.name = ''
        self.position = ''

    def toRecord(self):
        return (
            self.brefid, 
            self.name, 
            self.position
        )

    def fromRecord(record):
        playerSchema = PlayerSchema()
        playerSchema.id = record[0]
        playerSchema.brefid = record[1]
        playerSchema.name = record[2]
        playerSchema.position = record[3]
        return playerSchema