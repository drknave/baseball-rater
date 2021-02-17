class TeamSeasonSchema:
    def __init__(self):
        self.id = 0
        self.team = 0
        self.season = 0

    def toRecord(self):
        return (
            self.team, 
            self.season
        )

    def fromRecord(record):
        teamSeasonSchema = TeamSeasonSchema()
        teamSeasonSchema.id = record[0]
        teamSeasonSchema.team = record[1]
        teamSeasonSchema.season = record[2]
        return teamSeasonSchema