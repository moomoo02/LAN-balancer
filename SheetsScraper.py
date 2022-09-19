#!/usr/bin/env python
import gspread
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests
import sys

gc = gspread.service_account(filename="creds.json")

sh = gc.open('LAN-balancer-data').sheet1



class SheetsScraper:
    def __init__(self, sheetUrl):
        self.convertSheetToCsv(sheetUrl)
        self.data = "data.csv"
        self.rankScore = {"Iron4": -1, "Iron3": -1, "Iron2": -1, "Iron1": -1,
                          "Bronze4": 0, "Bronze3": 0, "Bronze2": 0, "Bronze1": 0, 
                          "Silver4": 0, "Silver3": 0, "Silver2": 0, "Silver1": 0, 
                          "Gold4": 1, "Gold3": 1, "Gold2": 2, "Gold1": 2,
                          "Plat4": 3, "Plat3": 3, "Plat2": 4, "Plat1": 4,
                          "Diamond4": 5, "Diamond3": 5, "Diamond2": 6, "Diamond1": 6,
                          "Master": 7, "Challenger": 8, "Unranked": 0}

    #Get the names of everyone on the sheets and returns a list of names
    def convertSheetToCsv(self,sheetURL):
        html = requests.get(sheetURL).text
        soup = BeautifulSoup(html, "lxml")
        table = soup.find_all("table")[0]
        
        with open("data.csv", "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])

    #Returns a list of names
    def getNames(self):
        df = pd.read_csv(self.data, encoding='cp1252')
        names = df['Name'] #you can also use df['column_name']

        #Filter out nan
        res = []
        for name in names:
            if not pd.isnull(name):
                res.append(name)
        return res

    #Gets all signed-up IGNS
    def getIgns(self):
        df = pd.read_csv(self.data, encoding='cp1252')
        igns = df['In-Game/Summoner Name'] #you can also use df['column_name']

        #Filter out nan
        res = []
        for ign in igns:
            if not pd.isnull(ign):
                res.append(ign)
        return res

    #Gets number of participants
    def getSize(self):
        res = self.getNames()
        return len(res)

    #Gets list of player ranks 
    def getRanks(self):
        df = pd.read_csv(self.data, encoding='cp1252')
        ranks = df['Peak Season 11 or 12 Rank '] #you can also use df['column_name']

        #Filter out nan
        res = []
        for rank in ranks:
            if not pd.isnull(rank):
                res.append(rank)
        return res

    #Return dictionary of key: ign, value: rank
    def getPlayers(self):
        #Get list of igns
        igns = self.getIgns();
        #Get list of ranks converted to integers
        None



    



SS = SheetsScraper("https://docs.google.com/spreadsheets/d/1h3ax4sytEZDduxuduNwzYCiZr4PQu3z332Yp70wWPJU/edit?usp=sharing")
ranks = SS.getRanks()

for rank in ranks:
    print(rank)
print(SS.getSize())