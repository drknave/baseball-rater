from db.TeamSeasonsTable import TeamSeasonsTable
from InquirerPy import prompt
import os

class TeamSeasonSelection:
    def getValue(teamId):
        teamSeasonsForTeam = TeamSeasonsTable.retrieveByTeam(teamId)
        if len(teamSeasonsForTeam) > 0:
            teamSeasonsForm = TeamSeasonSelection.buildForm(teamSeasonsForTeam)
            return int(prompt(teamSeasonsForm)['season'])
        return None

    def buildForm(teamSeasons):
        return [
            {
                'type': 'list',
                'name': 'season',
                'message': 'Select a season',
                'choices': list(map(lambda teamSeason: {'name': str(teamSeason.season), 'value': str(teamSeason.id)}, teamSeasons))
            }
        ]
