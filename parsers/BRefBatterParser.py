from data_objects.domain.BattingSeason import BattingSeason
from data_objects.domain.Player import Player

class BRefBatterParser:
    def __init__(self, rowProperties):
        self.properties = rowProperties

    def parse(self):
        battingSeason = BattingSeason()
        battingSeason.player = self.__parsePlayer()
        battingSeason.games =  int(self.__getProperty('G', 0))
        battingSeason.atbats = int(self.__getProperty('AB', 0))
        battingSeason.hits = int(self.__getProperty('H', 0))
        battingSeason.doubles = int(self.__getProperty('2B', 0))
        battingSeason.triples = int(self.__getProperty('3B', 0))
        battingSeason.homeruns = int(self.__getProperty('HR', 0))
        battingSeason.strikeouts = int(self.__getProperty('SO', 0))
        battingSeason.walks = int(self.__getProperty('BB', 0))
        battingSeason.steals = int(self.__getProperty('SB', 0))
        return battingSeason

    def __parsePlayer(self):
        player = Player()
        player.brefid = self.__getProperty('data-append-csv', '')
        player.name = self.__getProperty('player', '')
        player.position = self.__getProperty('pos', '')
        return player

    def __getProperty(self, property, defaultValue=None):
        if property in self.properties:
            return self.properties[property]
        return defaultValue