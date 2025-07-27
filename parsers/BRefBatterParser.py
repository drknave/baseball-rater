from data_objects.domain.BattingSeason import BattingSeason
from data_objects.domain.Player import Player

class BRefBatterParser:
    def __init__(self, rowProperties):
        self.properties = rowProperties

    def parse(self):
        battingSeason = BattingSeason()
        battingSeason.player = self.__parsePlayer()
        battingSeason.games =  int(self.__getProperty('b_games', 0))
        battingSeason.atbats = int(self.__getProperty('b_ab', 0))
        battingSeason.hits = int(self.__getProperty('b_h', 0))
        battingSeason.doubles = int(self.__getProperty('b_doubles', 0))
        battingSeason.triples = int(self.__getProperty('b_triples', 0))
        battingSeason.homeruns = int(self.__getProperty('b_hr', 0))
        battingSeason.strikeouts = int(self.__getProperty('b_so', 0))
        battingSeason.walks = int(self.__getProperty('b_bb', 0))
        battingSeason.steals = int(self.__getProperty('b_sb', 0))
        return battingSeason

    def __parsePlayer(self):
        player = Player()
        player.brefid = self.__getProperty('data-append-csv', '')
        player.name = self.__getProperty('name_display', '')
        player.position = self.__getProperty('team_position', '')
        return player

    def __getProperty(self, property, defaultValue=None):
        if property in self.properties:
            return self.properties[property]
        return defaultValue