import sqlite3
from data_objects.db.TeamSchema import TeamSchema
from TeamRegistry import TeamRegistry

class TeamsTable:
    
    name = 'teams'

    def createTable():
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE teams
                    (
                        id         INTEGER PRIMARY KEY,
                        name       TEXT    UNIQUE NOT NULL,
                        code       CHAR(3) UNIQUE NOT NULL
                    );'''
        )

        connection.commit()
        connection.close()

    def populateTable():
        teamRecords = list(map(lambda team: (team[0], team[1]), TeamRegistry.getFullTeamListing()))
        
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.executemany('INSERT INTO teams(name, code) VALUES(?,?);', teamRecords)

        connection.commit()
        connection.close()

    def retrieve(id):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM teams WHERE id=?;', (id,))

        teamRecord = cursor.fetchone()
        connection.close()

        return TeamSchema.fromRecord(teamRecord)

    def retrieveId(teamSchema):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        
        cursor.execute('SELECT id FROM teams WHERE code=?;', (teamSchema.code,))
        id = cursor.fetchone()[0]
        connection.close()

        return id

