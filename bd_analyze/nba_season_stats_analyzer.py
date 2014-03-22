#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os
import glob
import sys 
import re
import argparse


# Argument parsing
parser = argparse.ArgumentParser(description='Jumpball analyze')
parser.add_argument('-s', '--season', action='store', help='Season in year', dest="year_season", required=True)
args = parser.parse_args()

season = args.year_season

#data_directory = "./nba_data"
data_directory = ("/Users/aidan.wong/Documents/mystuff/cs454/jumpball/bd_collect/nba_data/%s/" % season)
team_stat_path = './nba_data/*.csv'
team_stat_files = glob.glob(team_stat_path)

data_types = ['Height', 'Weight', 'WL_PERC']
num_data_types = len(data_types)

data_set=[]

def readTeamStats(file_name):
    dtypes = np.dtype({ 'names' : ('team', 'Height', 'Weight', 'WL_PERC'),
                        'formats' : ['S10', np.float, np.float, np.float] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
           usecols=(0,2,3,4), dtype=dtypes)

    #data_list = list(data)

    return data


def readTeamRecord(file_name):
    dtypes = np.dtype({ 'names' : ('team', 'WL_PERC'),
                        'formats' : ['S10', np.float] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
           usecols=(0,3), dtype=dtypes)

    return data


# Iterate through each NBA team stats file and output find the mean for each teams weight and height
def analyzeTeamStats():

    for root, dirs, files in os.walk(data_directory):
        for f in files:
            if f.endswith("agg_data.csv"):
                teamStats = readTeamStats(data_directory + f)
                
                teamStats_list =  zip(*teamStats)
                team = teamStats_list[0][0]
                ht_mean = np.array(teamStats_list[1], dtype=float).mean()
                wt_mean = np.array(teamStats_list[2], dtype=float).mean()
                wl_perc = teamStats_list[3][0]
    
                data = [ team, ht_mean, wt_mean, wl_perc ]
                print data_set+data
    

analyzeTeamStats()


