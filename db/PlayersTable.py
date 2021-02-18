import sqlite3
from data_objects.db.PlayerSchema import PlayerSchema

class PlayersTable:

    name = 'players'

    def createTable():
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE players
                    (
                        id         INTEGER PRIMARY KEY,
                        brefid     TEXT    UNIQUE NOT NULL,
                        name       TEXT    NOT NULL,
                        position   CHAR(2) NOT NULL
                    );'''
        )

        connection.commit()
        connection.close()

    def create(playerSchema):
        playerRecord = playerSchema.toRecord()
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO players(brefid,
                                              name,
                                              position)
                                       values(?,?,?);''', playerRecord)
        cursor.execute('SELECT id FROM players WHERE brefid=?;', (playerSchema.brefid,))

        playerId = cursor.fetchone()[0]
        connection.commit()
        connection.close()

        return playerId

    def retrieveById(id):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM players WHERE id=?;', (id,))
        playerRecord = cursor.fetchone()
        connection.close()

        return PlayerSchema.fromRecord(playerRecord) if playerRecord is not None else None

    def retrieveByBrefId(brefid):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
       
        cursor.execute('SELECT * FROM players WHERE brefid=?;', (brefid,))
        playerRecord = cursor.fetchone()
        connection.close()

        return PlayerSchema.fromRecord(playerRecord) if playerRecord is not None else None
