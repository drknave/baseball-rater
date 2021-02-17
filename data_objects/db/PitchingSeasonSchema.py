class PitchingSeasonSchema:
    def __init__(self):
        self.id = 0
        self.teamseason = 0
        self.player = 0
        self.innings = 0.00 
        self.era = 0.00
        self.strikeouts = 0 
        self.walks = 0

    def toRecord(self):
        return (
            self.teamseason, 
            self.player, 
            self.innings, 
            self.era, 
            self.strikeouts, 
            self.walks
        )

    def fromRecord(record):
        pitchingSeasonSchema = PitchingSeasonSchema()
        pitchingSeasonSchema.id = record[0]
        pitchingSeasonSchema.teamseason = record[1]
        pitchingSeasonSchema.player = record[2]
        pitchingSeasonSchema.innings = record[3]
        pitchingSeasonSchema.era = record[4]
        pitchingSeasonSchema.strikeouts = record[5]
        pitchingSeasonSchema.walks = record[6]
        return pitchingSeasonSchema