#!/usr/bin/python 



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re

# read PSVs into DataFrame
games = []
files = glob.glob('./nba-play-data/*.psv')
for f in files:
    df = pd.read_csv(f, sep='|')
    df['game_id'] = f.replace('.psv', '')
    games.append(df)

print 'Read {0} games'.format(len(games))


