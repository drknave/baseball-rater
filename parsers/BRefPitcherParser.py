from data_objects.domain.PitchingSeason import PitchingSeason
from data_objects.domain.Player import Player

class BRefPitcherParser:
    def __init__(self, rowProperties):
        self.properties = rowProperties

    def parse(self):
        pitchingSeason = PitchingSeason()
        pitchingSeason.player = self.__parsePlayer()
        pitchingSeason.innings = float(self.__getProperty('IP', 0.00))
        pitchingSeason.era = float(self.__getProperty('earned_run_avg', 0.00))
        pitchingSeason.strikeouts = int(self.__getProperty('SO', 0))
        pitchingSeason.walks = int(self.__getProperty('BB', 0))
        return pitchingSeason

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