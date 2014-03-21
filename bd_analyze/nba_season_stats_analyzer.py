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

ht_wt_mean_set=[]

def readTeamStats(file_name):
    dtypes = np.dtype({ 'names' : ('team', 'Height', 'Weight'),
                        'formats' : ['S10', np.float, np.float] })

    data = np.loadtxt(file_name, delimiter=',', skiprows=1,
           usecols=(0,2,3), dtype=dtypes)

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
            if f.endswith("weight.csv"):
                teamStats = readTeamStats(data_directory + f)
                
                teamStats_list =  zip(*teamStats)
                team = teamStats_list[0][0]
                ht_mean = np.array(teamStats_list[1], dtype=float).mean()
                wt_mean = np.array(teamStats_list[2], dtype=float).mean()
    
                ht_wt_mean = [ team, ht_mean, wt_mean ]
                print ht_wt_mean_set+ht_wt_mean
    

analyzeTeamStats()


