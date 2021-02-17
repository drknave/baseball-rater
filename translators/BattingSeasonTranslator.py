from data_objects.db.BattingSeasonSchema import BattingSeasonSchema
from data_objects.domain.BattingSeason import BattingSeason
from db.PlayersTable import PlayersTable
from db.TeamSeasonsTable import TeamSeasonsTable
from translators.PlayerTranslator import PlayerTranslator
from translators.TeamSeasonTranslator import TeamSeasonTranslator

class BattingSeasonTranslator:
    def toSchema(battingSeason):
        schema = BattingSeasonSchema()
        schema.id = battingSeason.id
        schema.player = BattingSeasonTranslator.getPlayerId(battingSeason.player)
        schema.teamseason = BattingSeasonTranslator.getTeamSeasonId(battingSeason.teamSeason)
        schema.games = battingSeason.games
        schema.atbats = battingSeason.atbats
        schema.hits = battingSeason.hits
        schema.doubles = battingSeason.doubles
        schema.triples = battingSeason.triples
        schema.homeruns = battingSeason.homeruns
        schema.strikeouts = battingSeason.strikeouts
        schema.walks = battingSeason.walks
        schema.steals = battingSeason.steals
        return schema

    def toDomain(battingSeasonSchema):
        battingSeason = BattingSeason()
        battingSeason.id = battingSeasonSchema.id
        battingSeason.player = BattingSeasonTranslator.getPlayer(battingSeasonSchema.player)
        battingSeason.teamseason = BattingSeasonTranslator.getTeamSeason(battingSeasonSchema.teamseason)
        battingSeason.games = battingSeasonSchema.games
        battingSeason.atbats = battingSeasonSchema.atbats
        battingSeason.hits = battingSeasonSchema.hits
        battingSeason.doubles = battingSeasonSchema.doubles
        battingSeason.triples = battingSeasonSchema.triples
        battingSeason.homeruns = battingSeasonSchema.homeruns
        battingSeason.strikeouts = battingSeasonSchema.strikeouts
        battingSeason.walks = battingSeasonSchema.walks
        battingSeason.steals = battingSeasonSchema.steals
        return battingSeason

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