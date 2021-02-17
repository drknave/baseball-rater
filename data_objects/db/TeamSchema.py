class TeamSchema:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.code = ''

    def toRecord(self):
        return (
            self.name, 
            self.code
        )

    def fromRecord(record):
        teamSchema = TeamSchema()
        teamSchema.id = record[0]
        teamSchema.name = record[1]
        teamSchema.code = record[2]
        return teamSchema

    