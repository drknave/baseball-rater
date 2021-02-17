class BattingSeasonSchema:
    def __init__(self):
        self.id = 0
        self.player = 0    
        self.teamseason = 0
        self.games = 0
        self.atbats = 0 
        self.hits = 0
        self.doubles = 0  
        self.triples = 0
        self.homeruns = 0
        self.strikeouts = 0
        self.walks = 0
        self.steals = 0

    def toRecord(self):
        return (
            self.teamseason,
            self.player,
            self.games, 
            self.atbats, 
            self.hits, 
            self.doubles, 
            self.triples, 
            self.homeruns, 
            self.strikeouts, 
            self.walks, 
            self.steals
        ) 

    def fromRecord(record):
        battingSeasonSchema = BattingSeasonSchema()
        battingSeasonSchema.id = record[0]
        battingSeasonSchema.player = record[2]
        battingSeasonSchema.teamseason = record[3]
        battingSeasonSchema.games = record[4]
        battingSeasonSchema.atbats = record[5]
        battingSeasonSchema.hits = record[6]
        battingSeasonSchema.doubles = record[7]
        battingSeasonSchema.triples = record[8]
        battingSeasonSchema.homeruns = record[9]
        battingSeasonSchema.strikeouts = record[10]
        battingSeasonSchema.walks = record[11]
        battingSeasonSchema.steals = record[12]
        return battingSeasonSchema