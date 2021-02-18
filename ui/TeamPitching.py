from db.PitchingSeasonsTable import PitchingSeasonsTable
from translators.PitchingSeasonTranslator import PitchingSeasonTranslator
from tabulate import tabulate

class TeamPitching:
    def display(teamSeasonId):
        pitchingSeasonsSchema = PitchingSeasonsTable.retrieveForTeamSeason(teamSeasonId)
        pitchingSeasons = list(map(PitchingSeasonTranslator.toDomain, pitchingSeasonsSchema))
        TeamPitching.printTable(pitchingSeasons)

    def printTable(pitchingSeasons):
        rows = list(map(lambda pitchingSeason: [
            pitchingSeason.player.name,
            pitchingSeason.player.position,
            pitchingSeason.innings,
            pitchingSeason.era,
            pitchingSeason.strikeouts,
            pitchingSeason.walks,
        ], pitchingSeasons))
        print(tabulate(rows, headers=[
            'Name', 
            'Position',
            'Innings',
            'ERA',
            'K',
            'BB'
        ]))