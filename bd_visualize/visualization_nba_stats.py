#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os
import glob
import sys 
import re
import cv2
import random


trainData = np.array([[2,4],[10,3],[4,5],[5,3],[2,1]])

labels = np.array(np.arange(30))
print labels

for i in range(0,5):
	r = lambda: random.randint(0,255)
	color = '#%02X%02X%02X' % (r(),r(),r())
	team_data = trainData[labels.ravel()==i]
	pyplot.scatter(team_data[:,0],team_data[:,1],80,color,'^')


pyplot.show()
