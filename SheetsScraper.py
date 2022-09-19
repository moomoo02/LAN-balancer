#!/usr/bin/env python
import gspread
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests
import sys

gc = gspread.service_account(filename="creds.json")

sh = gc.open('LAN-balancer-data').sheet1


sh.append_row(['first','second'])

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
                          "Master": 7, "Challenger": 8}
                          
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

    #Return dictionary of key: ign, value: rank
    def getPlayers(self):
        None



    



SS = SheetsScraper("https://docs.google.com/spreadsheets/d/1h3ax4sytEZDduxuduNwzYCiZr4PQu3z332Yp70wWPJU/edit?usp=sharing")
names = SS.getNames()

for name in names:
    print(name)