from TeamRegistry import TeamRegistry
from capture.TeamSeasonCapture import TeamSeasonCapture
from data_objects.db.TeamSchema import TeamSchema
from db.DatabaseSetup import DatabaseSetup
from db.TeamsTable import TeamsTable

def initializeDatabase():
    DatabaseSetup.setup()

def testStats():
    schema = TeamSchema()
    schema.name = TeamRegistry.DETROIT[0]
    schema.code = TeamRegistry.DETROIT[1]

    teamId = TeamsTable.retrieveId(schema)
    
    seasonLoader2020 = TeamSeasonCapture(teamId, 2020)
    seasonLoader2020.capture()
    seasonLoader2019 = TeamSeasonCapture(teamId, 2019)
    seasonLoader2019.capture()

initializeDatabase()
testStats()
