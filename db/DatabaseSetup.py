import sqlite3
from db.TeamsTable import TeamsTable
from db.TeamSeasonsTable import TeamSeasonsTable
from db.PlayersTable import PlayersTable
from db.BattingSeasonsTable import BattingSeasonsTable
from db.PitchingSeasonsTable import PitchingSeasonsTable

class DatabaseSetup:
    def setup():
        if not DatabaseSetup.tableExists(TeamsTable.name):
            TeamsTable.createTable()
            TeamsTable.populateTable()
        if not DatabaseSetup.tableExists(TeamSeasonsTable.name):
            TeamSeasonsTable.createTable()
        if not DatabaseSetup.tableExists(PlayersTable.name):
            PlayersTable.createTable()
        if not DatabaseSetup.tableExists(BattingSeasonsTable.name):
            BattingSeasonsTable.createTable()
        if not DatabaseSetup.tableExists(PitchingSeasonsTable.name):
            PitchingSeasonsTable.createTable()

    def tableExists(tableName):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type=? AND name=?;', ('table', tableName))

        names = cursor.fetchone()
        exists = names is not None and len(names) > 0
        
        connection.close()
        return exists
        
