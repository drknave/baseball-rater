from data_objects.ratings.BattingSeasonRatings import BattingSeasonRatings
from db.BattingSeasonsTable import BattingSeasonsTable
from translators.BattingSeasonTranslator import BattingSeasonTranslator

class BattingSeasonRater:
    def rate(season):
        ratings = BattingSeasonRatings()
        ratings.player = season.player
        ratings.average = BattingSeasonRater.getAverageQuality(season)
        ratings.power = BattingSeasonRater.getPowerQuality(season)
        ratings.strikeouts = BattingSeasonRater.getStrikeoutQuality(season)
        ratings.walks = BattingSeasonRater.getWalkQuality(season)
        ratings.baserunning = BattingSeasonRater.getBaserunningQuality(season)
        return ratings

    def getAverageQuality(season):
        average = season.hits/season.atbats if season.atbats > 0 else 0
        if average > 0.4:
            return 'HERO and CHAMPION'
        elif average > 0.38:
            return 'SEMI-HERO and CHAMPION'
        elif average > 0.36:
            return 'CHAMPION'
        elif average > 0.34:
            return 'HERO and SEMI-CHAMPION'
        elif average > 0.32:
            return 'SEMI-HERO and SEMI-CHAMPION'
        elif average > 0.3:
            return 'SEMI-CHAMPION'
        elif average > 0.28:
            return 'HERO'
        elif average > 0.26:
            return 'SEMI-HERO'
        elif average > 0.24:
            return 'None'
        elif average > 0.22:
            return 'SEMI-UTILITY'
        elif average > 0.2:
            return 'UTILITY'
        elif average > 0.18:
            return 'SEMI-SAD SACK'
        elif average > 0.16:
            return 'SEMI-UTILITY and SEMI-SAD SACK'
        elif average > 0.14:
            return 'UTILITY AND SEMI-SAD SACK'
        elif average > 0.12:
            return 'SAD SACK'
        elif average > 0.1:
            return 'SEMI-UTILITY and SAD SACK'
        else:
            return 'UTILITY and SAD SACK'

    def getPowerQuality(season):
        hrs = season.homeruns if season.homeruns > 0 else 1
        doublesPerHr = season.doubles/hrs
        if hrs > 55:
            return 'HR KING and SLUGGER'
        elif hrs > 46:
            return 'SEMI-SLUGGER AND HR KING'
        elif hrs > 39:
            return 'SLUGGER and SEMI-HR-KING'
        elif hrs > 34:
            return 'HR KING'
        elif hrs > 24:
            return 'SLUGGER' if doublesPerHr > 1.25 else 'SEMI-SLUGGER and SEMI-HR KING'
        elif hrs > 16:
            return 'SEMI-SLUGGER' if doublesPerHr > 1.5 else 'SEMI-HR KING'
        elif hrs > 7:
            return 'None'
        elif hrs > 2:
            return 'SEMI-SCRAPPER'
        else:
            return 'SCRAPPER'

    def getStrikeoutQuality(season):
        strikeouts = season.strikeouts if season.strikeouts > 0 else 1
        atBatsPerStrikeout = season.atbats/strikeouts
        if atBatsPerStrikeout > 19:
            return 'GOOD EYE'
        elif atBatsPerStrikeout > 13:
            return 'SEMI-GOOD EYE'
        elif atBatsPerStrikeout > 9:
            return 'None'
        elif atBatsPerStrikeout > 6:
            return 'SEMI-WHIFFER'
        else:
            return 'WHIFFER'

    def getWalkQuality(season):
        walks = season.walks if season.walks > 0 else 1
        atBatsPerWalk = season.atbats/walks
        if atBatsPerWalk > 19:
            return 'EAGER'
        elif atBatsPerWalk > 14:
            return 'SEMI-EAGER'
        elif atBatsPerWalk > 9:
            return 'None'
        elif atBatsPerWalk > 6:
            return 'SEMI-PATIENT'
        else:
            return 'PATIENT'

    def getBaserunningQuality(season):
        steals = season.steals if season.steals > 0 else 1
        atBatsPerSteal = season.atbats/steals
        if atBatsPerSteal > 499:
            return 'STOIC'
        elif atBatsPerSteal > 99:
            return 'SEMI-STOIC'
        elif atBatsPerSteal > 49:
            return 'None'
        elif atBatsPerSteal > 19:
            return 'SEMI-ACTIVE'
        elif atBatsPerSteal > 9:
            return 'ACTIVE'
        else:
            return 'DOUBLE ACTIVE'
    