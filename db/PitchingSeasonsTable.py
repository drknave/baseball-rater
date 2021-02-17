import sqlite3
from data_objects.db.PitchingSeasonSchema import PitchingSeasonSchema

class PitchingSeasonsTable:

    name = 'pitchingseasons'

    def createTable():
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE pitchingseasons
                    (
                        id         INTEGER PRIMARY KEY,
                        teamseason INTEGER NOT NULL,
                        player     INTEGER NOT NULL,
                        innings    REAL    NOT NULL,
                        era        REAL    NOT NULL,
                        strikeouts INT     NOT NULL,
                        walks      INT     NOT NULL,
                        FOREIGN KEY(teamseason) REFERENCES teamseasons(id)
                        FOREIGN KEY(player) REFERENCES player(id)
                    );'''
        )

        connection.commit()
        connection.close()

    def createMany(pitchingSeasons):
        pitchingSeasonRecords = list(map(lambda pitchingSeasonSchema: pitchingSeasonSchema.toRecord(), pitchingSeasons))
        
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.executemany('''INSERT INTO pitchingseasons(teamseason, 
                                                          player,
                                                          innings, 
                                                          era, 
                                                          strikeouts,
                                                          walks)
                                            values(?,?,?,?,?,?);''', pitchingSeasonRecords)

        connection.commit()
        connection.close()

    def retrieveForTeamSeason(teamSeasonId):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pitchingseasons WHERE teamseason=?;', (teamSeasonId,))

        pitchingSeasonRecords = cursor.fetchall()

        connection.close()

        return list(map(lambda record: PitchingSeasonSchema.fromRecord(record)), pitchingSeasonRecords)

    def retrieveById(id):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pitchingseasons WHERE id=?;', (id,))

        pitchingSeasonRecord = cursor.fetchone()
        connection.close()

        return PitchingSeasonsTable.createPitchingSeasonFromRecord(pitchingSeasonRecord) if pitchingSeasonRecord is not None else None

    def deleteForTeamSeason(teamSeason):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pitchingseasons WHERE teamseason=?;', (teamSeason,))
        connection.commit()
        connection.close()
