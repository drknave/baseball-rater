from ui.views.GenerateRatings import GenerateRatings
from ui.views.LoadTeamSeason import LoadTeamSeason
from ui.views.ViewTeamSeason import ViewTeamSeason
from InquirerPy import prompt
import os

class MainMenu:
    options = [
        {
            'type': 'list',
            'name': 'function',
            'message': 'What would you like to do?',
            'choices': ['Load team season stats', 'View team season stats', 'Generate player ratings', 'Quit']
        }
    ]

    def display():
        MainMenu.clearScreen()
        mainMenuSelection = prompt(MainMenu.options)

        if mainMenuSelection['function'] == 'Load team season stats':
            LoadTeamSeason.display()
            MainMenu.display()
        elif mainMenuSelection['function'] == 'View team season stats':
            ViewTeamSeason.display()
            MainMenu.display()
        elif mainMenuSelection['function'] ==  'Generate player ratings':
            GenerateRatings.display()
            MainMenu.display()
        elif mainMenuSelection['function'] == 'Quit':
            quit()
    
    def clearScreen():
        _ = os.system("cls")
        _ = os.system("clear")
