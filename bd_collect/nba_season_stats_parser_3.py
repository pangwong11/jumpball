#!/usr/bin/python

# Python module to collect data from basketball-reference.com and output the collected data in a CSV formatted file

import urllib2
import argparse
from bs4 import BeautifulSoup
import csv
import re
import os
import itertools as IT

# Variables
data_directory="nba_data"

# Argument parsing
parser = argparse.ArgumentParser(description='Jumpball collect')
parser.add_argument('-s', '--season', action='store', help='Season in year', dest="year_season", required=True)
parser.add_argument('-t', '--team', action='store', help='NBA Team', dest="nba_team", required=True)
args = parser.parse_args()

season = args.year_season
team = args.nba_team
print season
print team

page = urllib2.urlopen("http://www.basketball-reference.com/teams/%s/%s.html" % (team, season ))

season_data_directory=("%s/%s" % (data_directory, season) )

if not os.path.exists(data_directory):
    os.makedirs(data_directory)
if not os.path.exists(season_data_directory):
    os.makedirs(season_data_directory)

player_stats_file = "./%s/season_%s_%s_players_height_weight.csv" % (season_data_directory, season, team )
team_stats_file = "./%s/season_%s_%s_record.csv" % (season_data_directory, season, team )
agg_stats_file = "./%s/season_%s_%s_agg_data.csv" % (season_data_directory, season, team)

stat_files = ['player_stats_file', 'team_stats_file']


f1 = csv.writer(open(player_stats_file, 'w') )
f2 = csv.writer(open(team_stats_file, 'w') )
f3 = csv.writer(open(agg_stats_file, 'w') )

# CSV file header
f1.writerow(["team", "name" ,"ht", "wt"])
f2.writerow(["team", "win", "loss", "wl_perc"])
f3.writerow(["team", "name", "ht", "wt" ,"wl_perc"])

def getStatsFromWeb(page):


    content = page.read()

    soup = BeautifulSoup(content)


    for elem in soup(text=re.compile(r'Record:')):
        record = elem.next_element.strip().split(',', 1)[0]
        w_record = float(record.split('-', 1)[0])
        l_record = float(record.split('-', 1)[1])

    print w_record
    print l_record
    wl_perc = w_record / (w_record + l_record)
    print wl_perc
    
    f2.writerow([team, w_record, l_record, wl_perc])

    roster_table = soup.find('table', id="roster")
    rows = roster_table.findAll('tr')

    for tr in rows:
        cells = tr.findAll('td')
        #if len(cells) > 0:
        if len(cells) == 0:
            continue

        #print cells
        name = cells[1].find(text=True)
        ht = cells[3].find(text=True).replace("-", ".")
        wt = cells[4].find(text=True)
    
        f1.writerow([team, name, ht, wt])
        f3.writerow([team, name, ht, wt, wl_perc])


getStatsFromWeb(page);



