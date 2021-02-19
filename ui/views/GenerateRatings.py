from translators.BattingSeasonTranslator import BattingSeasonTranslator
from translators.PitchingSeasonTranslator import PitchingSeasonTranslator
from db.BattingSeasonsTable import BattingSeasonsTable
from db.PitchingSeasonsTable import PitchingSeasonsTable
from db.TeamSeasonsTable import TeamSeasonsTable
from raters.BattingSeasonRater import BattingSeasonRater
from raters.PitchingSeasonRater import PitchingSeasonRater
from ui.components.TeamSelection import TeamSelection
from ui.components.TeamSeasonSelection import TeamSeasonSelection
from tabulate import tabulate

class GenerateRatings:
    def display():
        teamId = TeamSelection.getValue()
        teamSeason = TeamSeasonSelection.getValue(teamId)
        if teamSeason is not None:
            ratedBattingSeasons = GenerateRatings.getBattingSeasons(teamSeason)
            ratedPitchingSeasons = GenerateRatings.getPitchingSeasons(teamSeason)
            GenerateRatings.printRatings(ratedBattingSeasons, ratedPitchingSeasons)
        else:
            print('No season data loaded for team')
        input('Press any key to continue...')

    def getBattingSeasons(teamSeason):
        battingSeasonsSchema = BattingSeasonsTable.retrieveForTeamSeason(teamSeason)
        battingSeasons = list(map(BattingSeasonTranslator.toDomain, battingSeasonsSchema))
        return list(map(BattingSeasonRater.rate, battingSeasons))

    def getPitchingSeasons(teamSeason):
        pitchingSeasonsSchema = PitchingSeasonsTable.retrieveForTeamSeason(teamSeason)
        pitchingSeasons = list(map(PitchingSeasonTranslator.toDomain, pitchingSeasonsSchema))
        return list(map(PitchingSeasonRater.rate, pitchingSeasons))

    def printRatings(ratedBattingSeasons, ratedPitchingSeasons):
        GenerateRatings.displayBattingRatings(ratedBattingSeasons)
        print('')
        GenerateRatings.displayPitchingRatings(ratedPitchingSeasons)
        print('')

    def displayBattingRatings(ratedBattingSeasons):
        rows = list(map(lambda battingSeason: [
            battingSeason.player.name,
            battingSeason.player.position,
            battingSeason.average,
            battingSeason.power,
            battingSeason.strikeouts,
            battingSeason.baserunning
        ], ratedBattingSeasons))

        print('Batting Ratings')
        print(tabulate(rows, headers=[
            'Name', 
            'Position',
            'Average',
            'Power',
            'Strikeouts',
            'Baserunning'
        ]))

    def displayPitchingRatings(ratedPitchingSeasons):
        rows = list(map(lambda pitchingSeason: [
            pitchingSeason.player.name,
            pitchingSeason.player.position,
            pitchingSeason.era,
            pitchingSeason.power,
            pitchingSeason.control
        ], ratedPitchingSeasons))

        print('Pitching Ratings')
        print(tabulate(rows, headers=[
            'Name', 
            'Position',
            'ERA',
            'Power',
            'Control'
        ]))
