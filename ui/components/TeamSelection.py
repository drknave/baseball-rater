from db.TeamsTable import TeamsTable
from InquirerPy import prompt
import os

class TeamSelection:
    def getValue():
        teamsForm = TeamSelection.buildForm()
        return prompt(teamsForm)['team']

    def buildForm():
        return [
            {
                'type': 'list',
                'name': 'team',
                'message': 'Select a team',
                'choices': list(map(lambda team: {'name': team.name, 'value': team.id}, TeamsTable.retrieveAll()))
            }
        ]