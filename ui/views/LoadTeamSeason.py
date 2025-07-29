from capture.TeamSeasonCapture import TeamSeasonCapture
from ui.components.TeamSelection import TeamSelection
from InquirerPy import prompt
import os

class LoadTeamSeason:
    def display():
        teamId = TeamSelection.getValue()
        season = LoadTeamSeason.getSeason()
        teamSeasonCapture = TeamSeasonCapture(teamId, season)
        teamSeasonCapture.capture()

    def getSeason():
        seasonPrompt = [
            {
                'type': 'input',
                'name': 'season',
                'message': 'Enter a season year'
            }
        ]

        season = prompt(seasonPrompt)['season']

        if not season.isnumeric() or len(season) != 4:
            print('Invalid year')
            input('Press any key to try again...')
            LoadTeamSeason.getSeason()
        else:
            return int(season)
