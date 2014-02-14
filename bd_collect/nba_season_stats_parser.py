#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import csv

page = urllib2.urlopen("http://www.basketball-reference.com/leagues/NBA_2012_advanced.html")
content = page.read()

soup = BeautifulSoup(content)

table = soup.find('table', id="advanced")
rows = table.findAll('tr')

f = csv.writer(open('output.csv', 'w'))

# CSV file header
f.writerow(["name" ,"pos" ,"age" ,"team" ,"games" ,"minutes" ,"eff_rating" ,"ts_perc" ,"efg_perc" ,"ft_rate" ,"threept_rate" ,"orb_perc" ,"drb_perc" ,"trb_perc" ,"ast_perc" ,"stl_perc" ,"blk_perc" ,"tov_perc" ,"usg_perc" ,"off_rate" ,"def_rate" ,"ofw_share" ,"defw_share" ,"win_share" ,"win48_share"])

for tr in rows:
  cells = tr.findAll('td')
  if len(cells) == 26:
    name = cells[1].find(text=True)
    pos = cells[2].find(text=True)
    age = cells[3].find(text=True)
    team = cells[4].find(text=True)
    games = cells[5].find(text=True)
    minutes = cells[6].find(text=True)
    eff_rating = cells[7].find(text=True)
    ts_perc = cells[8].find(text=True)
    efg_perc = cells[9].find(text=True)
    ft_rate = cells[10].find(text=True)
    threept_rate = cells[11].find(text=True)
    orb_perc = cells[12].find(text=True)
    drb_perc = cells[13].find(text=True)
    trb_perc = cells[14].find(text=True)
    ast_perc = cells[15].find(text=True)
    stl_perc = cells[16].find(text=True)
    blk_perc = cells[17].find(text=True)
    tov_perc = cells[18].find(text=True)
    usg_perc = cells[19].find(text=True)
    off_rate = cells[20].find(text=True)
    def_rate = cells[21].find(text=True)
    ofw_share = cells[22].find(text=True)
    defw_share = cells[23].find(text=True)
    win_share = cells[24].find(text=True)
    win48_share = cells[25].find(text=True)

    f.writerow([name, pos, age, team, games, minutes, eff_rating, ts_perc, efg_perc, ft_rate, threept_rate, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, blk_perc, tov_perc, usg_perc, off_rate, def_rate, ofw_share, defw_share, win_share, win48_share])



