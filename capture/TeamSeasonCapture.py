from data_objects.db.TeamSeasonSchema import TeamSeasonSchema
from data_objects.domain.TeamSeason import TeamSeason
from db.BattingSeasonsTable import BattingSeasonsTable
from db.PitchingSeasonsTable import PitchingSeasonsTable
from db.TeamsTable import TeamsTable
from db.TeamSeasonsTable import TeamSeasonsTable
from parsers.BRefTeamSeasonParser import BRefTeamSeasonParser
from scrapers.BRefTeamSeasonScraper import BRefTeamSeasonScraper
from translators.BattingSeasonTranslator import BattingSeasonTranslator
from translators.PitchingSeasonTranslator import PitchingSeasonTranslator
from translators.TeamSeasonTranslator import TeamSeasonTranslator

class TeamSeasonCapture:
    def __init__(self, teamId, season):
        self.teamId = teamId
        self.season = season
        self.teamSeason = None

    def capture(self):
        source = self.__getTeamSeasonSource()
        self.__establishTeamSeason()
        teamParser = BRefTeamSeasonParser(source)
        battingSeasons = teamParser.parseBatters()
        pitchingSeasons = teamParser.parsePitchers()
        self.__writeBattingSeasons(battingSeasons)
        self.__writePitchingSeasons(pitchingSeasons)

    def __getTeamSeasonSource(self):
        scraper = BRefTeamSeasonScraper()
        teamCode = self.__getTeamCode()
        return scraper.getSource(teamCode, self.season)

    def __getTeamCode(self):
        team = TeamsTable.retrieve(self.teamId)
        return team.code

    def __establishTeamSeason(self):
        existingTeamSeason = self.__getExistingTeamSeason()
        self.teamSeason = self.__createTeamSeason() if existingTeamSeason is None else existingTeamSeason

    def __getExistingTeamSeason(self):
        return TeamSeasonsTable.retrieveByTeamAndSeason(self.teamId, self.season)

    def __createTeamSeason(self):
        teamSeasonSchema = TeamSeasonSchema()
        teamSeasonSchema.team = self.teamId
        teamSeasonSchema.season = self.season
        teamSeasonId = TeamSeasonsTable.create(teamSeasonSchema)
        teamSeasonSchema.id = teamSeasonId
        return TeamSeasonTranslator.toDomain(teamSeasonSchema)

    def __writeBattingSeasons(self, battingSeasons):
        battingSeasonsSchema = list(map(lambda battingSeason: self.__createBattingSeasonSchema(battingSeason), battingSeasons))
        BattingSeasonsTable.createMany(battingSeasonsSchema)

    def __createBattingSeasonSchema(self, battingSeason):
        battingSeason.teamSeason = self.teamSeason
        return BattingSeasonTranslator.toSchema(battingSeason)

    def __writePitchingSeasons(self, pitchingSeasons):
        pitchingSeasonsSchema = list(map(lambda pitchingSeason: self.__createPitchingSeasonSchema(pitchingSeason), pitchingSeasons))
        PitchingSeasonsTable.createMany(pitchingSeasonsSchema)

    def __createPitchingSeasonSchema(self, pitchingSeason):
        pitchingSeason.teamSeason = self.teamSeason
        return PitchingSeasonTranslator.toSchema(pitchingSeason)
