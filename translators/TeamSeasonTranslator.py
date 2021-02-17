from data_objects.db.TeamSeasonSchema import TeamSeasonSchema
from data_objects.domain.TeamSeason import TeamSeason

from db.TeamsTable import TeamsTable
from translators.TeamTranslator import TeamTranslator

class TeamSeasonTranslator:
    def toSchema(teamSeason):
        schema = TeamSeasonSchema()
        schema.id = teamSeason.id
        schema.team = TeamSeasonTranslator.getTeamId(teamSeason.team)
        schema.season = teamSeason.season
        return schema

    def toDomain(teamSeasonSchema):
        teamSeason = TeamSeason()
        teamSeason.id = teamSeasonSchema.id
        teamSeason.team = TeamSeasonTranslator.getTeam(teamSeasonSchema.team)
        teamSeason.season = teamSeasonSchema.season
        return teamSeason

    def getTeamId(team):
        teamSchema = TeamTranslator.toSchema(team)
        return TeamsTable.retrieveId(teamSchema)

    def getTeam(teamId):
        teamSchema = TeamsTable.retrieve(teamId)
        return TeamTranslator.toDomain(teamSchema)
