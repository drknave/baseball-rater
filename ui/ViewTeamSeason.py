from ui.TeamBatting import TeamBatting
from ui.TeamPitching import TeamPitching
from ui.TeamSelection import TeamSelection
from ui.TeamSeasonSelection import TeamSeasonSelection
from PyInquirer import prompt
import os

class ViewTeamSeason:
    def display():
        teamId = TeamSelection.getValue()
        teamSeason = TeamSeasonSelection.getValue(teamId)
        if teamSeason is not None:
            category = ViewTeamSeason.getStatCategory()
            if category is 'Batting':
                TeamBatting.display(teamSeason)
            elif category is 'Pitching':
                TeamPitching.display(teamSeason)
        else:
            print('No season data loaded for team')
        input('Press any key to continue...')

    def getStatCategory():
        categoryForm = [
            {
                'type': 'list',
                'name': 'stat_category',
                'message': 'Which stats do you want to see?',
                'choices': ['Batting', 'Pitching']
            }
        ]
        return prompt(categoryForm)['stat_category']
