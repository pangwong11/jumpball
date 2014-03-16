#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import os
import glob
import sys
import re

def readDataStdin():

  N_row = 0
  N_col = 0
  N_array = []

  E_row = 0 
  E_col = 0 
  E_array = []

  for line in sys.stdin:
      ta = line.strip().rstrip()
      if re.match(r'^N', ta):
        N_array.extend(ta.split(' '))
        #array = ta.split(' ')
        N_row += 1
        N_col = len(ta)
      elif re.match(r'^E', ta):
        E_array.extend(ta.split(' '))
        E_row += 1
        E_col = len(ta)        

#  print (row, col)
#  print array
  #dtypes = {'names' : ['field%i' %i for i in range(col)],
           #'formats' : ['S3', np.float, np.float, np.float, np.float]}

  #data = np.array(array, dtype=dtypes).reshape((row,col))
  N_data_list = np.array(N_array).reshape((N_row,5))
  E_data_list = np.array(E_array).reshape((E_row,4))

  return (N_data_list, E_data_list)


# Function to find min, max and standard deviation of node bias
def nodeAnalysis():
    
  N_array, E_array = readDataStdin()
  
  N_bias_min = np.array(N_array[:,4], dtype=float).min()
  N_bias_max = np.array(N_array[:,4], dtype=float).max()
  N_bias_mean = np.array(N_array[:,4], dtype=float).mean()
  N_bias_std = np.array(N_array[:,4], dtype=float).std()
  
  #print N_array[:,4]
  print (N_bias_min, N_bias_max, N_bias_mean, N_bias_std)
  #N_bias_min = N_array[:,4].mean(axis=0)

  #return N_bias_min

# Function to find the min, max and standard deviation of the edge weight
#def edgeAnalysis():

#  E_array = readDataStdin()

def read_file(file_name):
    #dtypes = np.dtype({ 'names' : ('type', '', '', '', 'events'),
    #                    'formats' : [np.int, np.float, np.float, np.float, 'S100'] })
    dtypes = np.dtype([('n_or_e', np.str_, 16)])

    data = np.array(np.loadtxt(file_name), dtype=dtypes)
#            converters = { 1 : float },
#            dtype=dtypes)
            #usecols=(0,1,2,3,7))

    return data

# ------------------------------------

min = 0 
max = 10000

for f in range(min,max):
  filename = '%04d' % f 

#for i
#data = read_file('./graph_data_files/0000')

nodeAnalysis()
#N_bias_min = nodeAnalysis()
#print N_bias_min
