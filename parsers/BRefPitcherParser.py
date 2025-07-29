from data_objects.domain.PitchingSeason import PitchingSeason
from data_objects.domain.Player import Player

class BRefPitcherParser:
    def __init__(self, rowProperties):
        self.properties = rowProperties

    def parse(self):
        pitchingSeason = PitchingSeason()
        pitchingSeason.player = self.__parsePlayer()
        pitchingSeason.innings = float(self.__getProperty('p_ip', 0.00))
        pitchingSeason.era = float(self.__getProperty('p_earned_run_avg', 0.00))
        pitchingSeason.strikeouts = int(self.__getProperty('p_so', 0))
        pitchingSeason.walks = int(self.__getProperty('p_bb', 0))
        return pitchingSeason

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