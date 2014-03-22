#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os
import glob
import sys 
import re
import argparse
import cv2
import random


# Argument parsing
parser = argparse.ArgumentParser(description='Jumpball analyze')
parser.add_argument('-s', '--season', action='store', help='Season in year', dest="year_season", required=True)
args = parser.parse_args()

season = args.year_season

#data_directory = "./nba_data"
data_directory = ("/Users/Song/Study/CS454/jumpball/bd_collect/nba_data/%s/" % season)
team_stat_path = './nba_data/*.csv'
team_stat_files = glob.glob(team_stat_path)

data_types = ['Height', 'Weight', 'WL_PERC']
num_data_types = len(data_types)

data_set=[]
team_labels_set = []
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
    
                data = [ht_mean, wt_mean,wl_perc]
                data_set.append(data)
                team_labels_set.append(team)
    #print data_set
    return data_set,team_labels_set

trainData, teamData = analyzeTeamStats()

trainData_array = np.array(trainData)

#print trainData_array

labels = np.array(np.arange(30))
for label, x, y in zip(teamData,trainData_array[:,0],trainData_array[:,1]):
    pyplot.annotate(label,xy =(x,y), xytext=(-20,20),textcoords = 'offset points', 
        ha ='right', va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', 
        alpha = 0.5),arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

for i in range(0,30):
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    team_data = trainData_array[labels.ravel()==i]
    pyplot.scatter(team_data[:,0],team_data[:,1],marker = 'o',s = team_data[:,2]*500,c = color,cmap = pyplot.get_cmap('Spectral'))
    #for label, x, y in zip(labels)

pyplot.show()

