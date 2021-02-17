from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from parsers import BRefTableParser
from parsers.BRefBatterParser import BRefBatterParser

battingTableStrainer = SoupStrainer(id="team_batting")

class BRefTeamBattingTableParser:
    def __init__(self, teamSource):
        self.soup = BeautifulSoup(teamSource, 'html.parser', parse_only=battingTableStrainer)

    def parse(self):
        if self.soup.tbody is not None:
            tableRows = self.soup.tbody.find_all('tr')
            playerRows = list(filter(BRefTableParser.isNotTableHeaderRow, tableRows))
            return list(map(self.__processBatter, playerRows))
        return []

    def __processBatter(self, playerRow):
        rowProperties = BRefTableParser.collectPropertiesForRow(playerRow)
        batterParser = BRefBatterParser(rowProperties)
        return batterParser.parse()
