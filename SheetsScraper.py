#!/usr/bin/env python
import gspread
from bs4 import BeautifulSoup
import csv
import requests
import sys

gc = gspread.service_account(filename="creds.json")

sh = gc.open('LAN-balancer-data').sheet1


sh.append_row(['first','second'])

class SheetsScraper:
    def __init__(self, sheetUrl):
        self.convertSheetToCsv(sheetUrl)

    #Get the names of everyone on the sheets and returns a list of names
    def convertSheetToCsv(self,sheetURL):
        html = requests.get(sheetURL).text
        soup = BeautifulSoup(html, "lxml")
        table = soup.find_all("table")[0]
        index = 0

        
        with open(str(index) + ".csv", "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
            index = index + 1

    



SS = SheetsScraper("https://docs.google.com/spreadsheets/d/1h3ax4sytEZDduxuduNwzYCiZr4PQu3z332Yp70wWPJU/edit?usp=sharing")
