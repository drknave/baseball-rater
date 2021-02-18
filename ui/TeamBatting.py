from db.BattingSeasonsTable import BattingSeasonsTable
from translators.BattingSeasonTranslator import BattingSeasonTranslator
from tabulate import tabulate

class TeamBatting:
    def display(teamSeasonId):
        battingSeasonsSchema = BattingSeasonsTable.retrieveForTeamSeason(teamSeasonId)
        battingSeasons = list(map(BattingSeasonTranslator.toDomain, battingSeasonsSchema))
        TeamBatting.printTable(battingSeasons)

    def printTable(battingSeasons):
        rows = list(map(lambda battingSeason: [
            battingSeason.player.name,
            battingSeason.player.position,
            battingSeason.games,
            battingSeason.atbats,
            battingSeason.hits,
            battingSeason.doubles,
            battingSeason.triples,
            battingSeason.homeruns,
            battingSeason.strikeouts,
            battingSeason.walks,
            battingSeason.steals
        ], battingSeasons))
        print(tabulate(rows, headers=[
            'Name', 
            'Position',
            'G',
            'AB',
            'H',
            '2B',
            '3B',
            'HR',
            'K',
            'BB',
            'SB'
        ]))