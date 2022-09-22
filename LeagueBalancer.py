class LeagueBalancer:

    def __init__(self, players={}):
        self.players = players
        self.playersListSize = len(players)
        self.numberOfTeams = len(players) / 5    
        self.roleMap = {"TOP": 0, "JG": 1, "MID": 2, "ADC": 3, "SUP": 4}
        
    #Returns the list of players and their rank score
    def getPlayers(self):
        return self.players

    #Returns the ideal score of a team
    def getTeamAverageScore(self):
        #Compute total score sum
        scoreSum = 0
        for ign,score in self.players.items():
            scoreSum += int(score)
        
        return scoreSum / self.numberOfTeams

    

