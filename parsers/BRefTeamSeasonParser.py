from parsers import BRefTableParser
from parsers.BRefTeamBattingTableParser import BRefTeamBattingTableParser
from parsers.BRefTeamPitchingTableParser import BRefTeamPitchingTableParser

class BRefTeamSeasonParser:
    def __init__(self, teamSource):
        self.teamSource = teamSource

    def parseBatters(self):
        teamBattingParser = BRefTeamBattingTableParser(self.teamSource)
        return teamBattingParser.parse()

    def parsePitchers(self):
        teamPitchingParser = BRefTeamPitchingTableParser(self.teamSource)
        return teamPitchingParser.parse()
