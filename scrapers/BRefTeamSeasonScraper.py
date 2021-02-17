import urllib.request

class BRefTeamSeasonScraper:
    def getSource(self, teamCode, season):
        response = urllib.request.urlopen("https://www.baseball-reference.com/teams/{}/{}.shtml".format(teamCode, season))
        return response.read()