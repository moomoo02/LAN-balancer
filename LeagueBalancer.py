from functools import cmp_to_key
import math

class LeagueBalancer:

    def __init__(self, players={}):
        self.players =  {k: v for k, v in sorted(players.items(), key=lambda item: item[1])} #Sorts the dictionary of players by rankScore
        self.playersListSize = len(players)
        self.numberOfTeams = round(len(players) / 5)    
        self.roleMap = {"TOP": 0, "JG": 1, "MID": 2, "ADC": 3, "SUP": 4, "FILL :)": -1}

    #Returns the list of players and their rank score
    def getPlayers(self):
        return self.players

    #Returns the result of the auto-balancer
    def balance(self):
        playerList = list(self.players.items())
        balanceResult = [["" for i in range(5)] for j in range(self.numberOfTeams)]
        averageList = [0 for i in range(self.numberOfTeams)]

        #Put top 5 in different teams
        curTeam = 0
        for i in range(len(self.players)-self.numberOfTeams, len(self.players)):
            ign, rank, priRole, secRole = playerList[i][0], playerList[i][1][0], self.roleMap[playerList[i][1][1]], self.roleMap[playerList[i][1][2]]
            balanceResult[curTeam][priRole] = ign
            averageList[curTeam] += rank
            curTeam += 1
        
        print(balanceResult)
        #Put worst 5 in different teams
        return balanceResult

    #Returns the ideal score of a team
    def getTeamAverageScore(self):
        #Compute total score sum
        scoreSum = 0
        for ign,score in self.players.items():
            scoreSum += int(score)
        
        return scoreSum / self.numberOfTeams
    




    

