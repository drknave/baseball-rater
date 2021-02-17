import sqlite3
from data_objects.db.TeamSeasonSchema import TeamSeasonSchema

class TeamSeasonsTable:

    name = 'teamseasons'

    def createTable():
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE teamseasons
                    (
                        id         INTEGER PRIMARY KEY,
                        team       INTEGER NOT NULL,
                        season     INTEGER NOT NULL,
                        FOREIGN KEY(team) REFERENCES teams(id),
                        UNIQUE(team, season)
                    );'''
        )

        connection.commit()
        connection.close()

    def create(teamSeasonSchema):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()

        cursor.execute('INSERT into teamseasons(team, season) VALUES(?,?);', (teamSeasonSchema.team, teamSeasonSchema.season))
        cursor.execute('SELECT id FROM teamseasons WHERE team=? AND season=?;', (teamSeasonSchema.team, teamSeasonSchema.season))

        teamSeasonId = cursor.fetchone()[0]
        connection.commit()
        connection.close()

        return teamSeasonId

    def retrieve(id):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM teamseasons WHERE id=?;', (id,))

        firstRow = cursor.fetchone()
        connection.close()

        if firstRow is None:
            return None
        return TeamSeasonSchema.fromRecord(firstRow)

    def retrieveByTeamAndSeason(team, season):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM teamseasons WHERE team=? AND season=?;', (team, season))

        firstRow = cursor.fetchone()
        connection.close()

        if firstRow is None:
            return None
        return TeamSeasonSchema.fromRecord(firstRow)

    def delete(team, season):
        connection = sqlite3.connect('baseball-rater.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM teamseasons WHERE team=? AND season=?;', (team, season))
        connection.commit()
        connection.close()
        