#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os
import glob
import sys 
import re


#data_directory = "./nba_data"
data_directory = "/Users/aidan.wong/Documents/mystuff/cs454/jumpball/bd_collect/nba_data/"
team_stat_path = './nba_data/*.csv'
team_stat_files = glob.glob(team_stat_path)

data_types = ['Height', 'Weight', 'WL_PERC']
num_data_types = len(data_types)


def readTeamStats(file_name):
    dtypes = np.dtype({ 'names' : ('team', 'Height', 'Weight'),
                        'formats' : ['S10', np.float, np.float] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
           usecols=(0,2,3), dtype=dtypes)

    data_list = list(data)

    print type(data)
    print type(data_list)
    return data


def readTeamRecord(file_name):
    dtypes = np.dtype({ 'names' : ('team', 'WL_PERC'),
                        'formats' : ['S10', np.float] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
           usecols=(0,3), dtype=dtypes)

    return data


def analyzeTeamStats():
    for root, dirs, files in os.walk(data_directory):
        for f in files:
            if f.endswith("weight.csv"):
                teamStats = readTeamStats(data_directory + f)
                
    teamStats_list =  zip(*teamStats)
    team = teamStats_list[0][0]
    #ht_mean = np.array(teamStats[:,2], dtype=float).mean()
    ht_mean = np.array(teamStats_list[1], dtype=float).mean()
    wt_mean = np.array(teamStats_list[2], dtype=float).mean()
    print team
    print ht_mean
    print wt_mean
    

#for f in team_stat_files:
#    print f
#   teamStats = readTeamStats(file)
#    teamStats = readTeamStats("./nba_stats/season_2011_BOS_players_height_weight.csv")

#    print teamStats
    

analyzeTeamStats()


