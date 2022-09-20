#!/usr/bin/env python

from LeagueBalancer import LeagueBalancer
from SheetsScraper import SheetsScraper


SS = SheetsScraper("https://docs.google.com/spreadsheets/d/1h3ax4sytEZDduxuduNwzYCiZr4PQu3z332Yp70wWPJU/edit?usp=sharing")
players = SS.getPlayers()

LB = LeagueBalancer(players)
print(LB.getPlayers())
print(LB.getTeamAverageScore())


#https://docs.google.com/spreadsheets/d/1PWUfp-dwh_t6uyfuJis6Tth2OmIVe3g_seySaZDyp_c/edit?usp=sharing