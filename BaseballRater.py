from db.DatabaseSetup import DatabaseSetup
from ui.views.MainMenu import MainMenu

def initializeDatabase():
    DatabaseSetup.setup()

def showMainMenu():
    MainMenu.display()

initializeDatabase()
showMainMenu()
