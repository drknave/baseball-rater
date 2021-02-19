from data_objects.ratings.PitchingSeasonRatings import PitchingSeasonRatings

class PitchingSeasonRater:
    def rate(season):
        ratings = PitchingSeasonRatings()
        ratings.player = season.player
        ratings.era = PitchingSeasonRater.getEraQuality(season)
        ratings.power = PitchingSeasonRater.getPowerQuality(season)
        ratings.control = PitchingSeasonRater.getControlQuality(season)
        return ratings
        
    def getEraQuality(season):
        era = season.era
        if era > 6.49:
            return 'STRUGGLER and WORKMAN'
        elif era > 5.74:
            return 'STRUGGLER'
        elif era > 5.24:
            return 'SEMI-STRUGGLER'
        elif era > 4.74: 
            return 'WORKMAN'
        elif era > 4.24:
            return 'SEMI-WORKMAN'
        elif era > 3.74:
            return 'None'
        elif era > 3.24:
            return 'SEMI-STAR'
        elif era > 2.74:
            return 'STAR'
        elif era > 2.24:
            return 'SEMI-ACE'
        elif era > 1.74:
            return 'ACE'
        else:
            return 'ACE and STAR'

    def getPowerQuality(season):
        innings = season.innings if season.innings > 0 else 0.1
        strikeoutsPerInning = season.strikeouts/innings
        if strikeoutsPerInning > 1.25:
            return 'DOUBLE FLASH'
        elif strikeoutsPerInning > (5/6):
            return 'FLASH'
        elif strikeoutsPerInning > 0.5:
            return 'SEMI-FLASH'
        else:
            return 'None'

    def getControlQuality(season):
        walks = season.walks if season.walks > 0 else 1
        inningsPerWalk = season.innings/walks
        if inningsPerWalk > 5.99:
            return 'DOUBLE CONTROL'
        elif inningsPerWalk > 3.99:
            return 'CONTROL'
        elif inningsPerWalk > 2.99:
            return 'SEMI-CONTROL'
        elif inningsPerWalk > 1.99:
            return 'None'
        elif inningsPerWalk > 1.49:
            return 'SEMI-WILD'
        elif inningsPerWalk > 0.99:
            return 'WILD'
        else:
            return 'DOUBLE WILD'
