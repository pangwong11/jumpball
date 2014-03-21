#!/usr/bin/python
# Python module to collect data from basketball-reference.com and output the collected data in a CSV formatted file

import urllib2
import argparse
from bs4 import BeautifulSoup
import csv
import re
import string
from string import Template

# Argument parsing
parser = argparse.ArgumentParser(description='Jumpball collect')
parser.add_argument('-s', '--season', action='store', help='Season in year', dest="year_season", required=True)
parser.add_argument('-t', '--team', action='store', help='NBA Team', dest="nba_team", required=True)
#args = vars(parser.parse_args())
args = parser.parse_args()

season = args.year_season
team = args.nba_team
print season
print team


page1 = urllib2.urlopen("http://www.nba.com/%s/roster/%s" % (team, season ))

f = csv.writer(open('season_%s_%s_players_height.csv' % (season, team), 'w'))

# CSV file header
f.writerow(["name" ,"ht", "wt", "team"])

def getStatsFromWeb(page):
    content = page.read()

    soup = BeautifulSoup(content)
    
    table = soup.find('table', summary="Team Roster")
#    rows = table.findAll('tr', recursive=False)
    rows = table.findAll('tr')
#    new_rows = string.replace(rows[0], ',', '\n')
    #new_rows = re.sub(',', '\n', rows[0])
    converted_rows = unicode.join(u'\n', map(unicode, rows))
#    print converted_rows

    new_soup = BeautifulSoup(converted_rows)
    new_rows = new_soup.findAll('td')    
    print type(new_rows)
    print new_rows

    for data in new_rows:
        print type(data)
        cells = data.findAll('td')
#        if len(cells) == 31
        print type(cells)
#        name = cells[1].find(text=True)
#        ht = cells[6].find(text=True).replace("-", ".")
#        ht = cells[3].find(text=True)
        wt = cells[7].find(text=True)
        print wt

        f.writerow([name, ht, wt])


getStatsFromWeb(page1);



