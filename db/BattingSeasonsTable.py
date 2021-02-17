import sqlite3
from data_objects.db.BattingSeasonSchema import BattingSeasonSchema

class BattingSeasonsTable:
    
    name = 'battingseasons'

    def createTable():
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE battingseasons
                    (
                        id         INTEGER PRIMARY KEY,
                        teamseason INTEGER NOT NULL,
                        player     INTEGER NOT NULL,
                        games      INT     NOT NULL,
                        atbats     INT     NOT NULL,
                        hits       INT     NOT NULL,
                        doubles    INT     NOT NULL,
                        triples    INT     NOT NULL,
                        homeruns   INT     NOT NULL,
                        strikeouts INT     NOT NULL,
                        walks      INT     NOT NULL,
                        steals     INT     NOT NULL,
                        FOREIGN KEY(player) REFERENCES players(id)
                        FOREIGN KEY(teamseason) REFERENCES teamseasons(id)
                    );'''
        )

        connection.close()

    def createMany(battingSeasons):
        battingSeasonRecords = list(map(lambda battingSeasonSchema: battingSeasonSchema.toRecord(), battingSeasons))
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.executemany('''INSERT INTO battingseasons(teamseason, 
                                                         player,
                                                         games, 
                                                         atbats, 
                                                         hits,
                                                         doubles,
                                                         triples,
                                                         homeruns,
                                                         strikeouts,
                                                         walks,
                                                         steals)
                                                  values(?,?,?,?,?,?,?,?,?,?,?);''', battingSeasonRecords)

        connection.commit()
        connection.close()

    def retrieveForTeamSeason(teamSeasonId):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM battingseasons WHERE teamseason=?;', (teamSeasonId,))

        battingSeasonRecords = cursor.fetchall()

        connection.commit()
        connection.close()

        return list(map(lambda record: BattingSeasonSchema.fromRecord(record)), battingSeasonRecords)

    def deleteForTeamSeason(teamSeasonId):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM battingseasons WHERE teamseason=?;', (teamSeasonId,))
        connection.commit()
        connection.close()
