from data_objects.db.PlayerSchema import PlayerSchema
from data_objects.domain.Player import Player

class PlayerTranslator:
    def toSchema(player):
        schema = PlayerSchema()
        schema.id = player.id
        schema.brefid = player.brefid
        schema.name = player.name
        schema.position = player.position
        return schema

    def toDomain(playerSchema):
        player = Player()
        player.id = playerSchema.id
        player.brefid = playerSchema.brefid
        player.name = playerSchema.name
        player.position = playerSchema.position
        return player