from data_objects.db.TeamSchema import TeamSchema
from data_objects.domain.Team import Team

class TeamTranslator:
    def toSchema(team):
        schema = TeamSchema()
        schema.id = team.id
        schema.name = team.name
        schema.code = team.code
        return schema

    def toDomain(schema):
        return Team(schema.id, schema.name, schema.code)
