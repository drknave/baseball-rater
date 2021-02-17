from data_objects.db.PitchingSeasonSchema import PitchingSeasonSchema
from data_objects.domain.PitchingSeason import PitchingSeason
from db.PlayersTable import PlayersTable
from db.TeamSeasonsTable import TeamSeasonsTable
from translators.PlayerTranslator import PlayerTranslator
from translators.TeamSeasonTranslator import TeamSeasonTranslator

class PitchingSeasonTranslator:
    def toSchema(pitchingSeason):
        schema = PitchingSeasonSchema()
        schema.id = pitchingSeason.id
        schema.player = PitchingSeasonTranslator.getPlayerId(pitchingSeason.player)
        schema.teamseason = PitchingSeasonTranslator.getTeamSeasonId(pitchingSeason.teamSeason)
        schema.innings = pitchingSeason.innings
        schema.era = pitchingSeason.era
        schema.strikeouts = pitchingSeason.strikeouts
        schema.walks = pitchingSeason.walks
        return schema

    def toDomain(pitchingSeasonSchema):
        pitchingSeason = PitchingSeason()
        pitchingSeason.id = pitchingSeasonSchema.id
        pitchingSeason.player = PitchingSeasonTranslator.getPlayer(pitchingSeasonSchema.player)
        pitchingSeason.teamseason = PitchingSeasonTranslator.getTeamSeason(pitchingSeasonSchema.teamseason)
        pitchingSeason.innings = pitchingSeasonSchema.innings
        pitchingSeason.era = pitchingSeasonSchema.era
        pitchingSeason.strikeouts = pitchingSeasonSchema.strikeouts
        pitchingSeason.walks = pitchingSeasonSchema.walks
        return pitchingSeason

    def getPlayerId(player):
        if player.id > 0:
            return player.id
        
        fromTable = PlayersTable.retrieveByBrefId(player.brefid)
        if fromTable is not None:
            return fromTable.id

        playerSchema = PlayerTranslator.toSchema(player)
        return PlayersTable.create(playerSchema)

    def getPlayer(playerId):
        playerSchema = PlayersTable.retrieveById(playerId)
        return PlayerTranslator.toDomain(playerSchema)

    def getTeamSeasonId(teamSeason):
        if teamSeason.id > 0:
            return teamSeason.id
        
        teamSeasonSchema = TeamSeasonTranslator.toSchema(teamSeason)
        fromTable = TeamSeasonsTable.retrieveByTeamAndSeason(teamSeasonSchema.team, teamSeasonSchema.season)
        if fromTable is not None:
            return fromTable.id

        return TeamSeasonsTable.create(teamSeasonSchema)

    def getTeamSeason(teamSeasonId):
        teamSeasonSchema = TeamSeasonsTable.retrieve(teamSeasonId)
        return TeamSeasonTranslator.toDomain(teamSeasonSchema)