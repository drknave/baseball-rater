from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from parsers import BRefTableParser
from parsers.BRefPitcherParser import BRefPitcherParser

pitchingTableStrainer = SoupStrainer(id="team_pitching")

class BRefTeamPitchingTableParser:
    def __init__(self, teamSource):
        self.soup = BeautifulSoup(teamSource, 'html.parser', parse_only=pitchingTableStrainer)

    def parse(self):
        if self.soup.tbody is not None:
            tableRows = self.soup.tbody.find_all('tr')
            playerRows = list(filter(BRefTableParser.isNotTableHeaderRow, tableRows))
            return list(map(self.__processPitcher, playerRows))
        return []

    def __processPitcher(self, playerRow):
        rowProperties = BRefTableParser.collectPropertiesForRow(playerRow)
        pitcherParser = BRefPitcherParser(rowProperties)
        return pitcherParser.parse()

    