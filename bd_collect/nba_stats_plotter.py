#!/usr/bin/python

# Python module to collect data from basketball-reference.com and output the collected data in a CSV formatted file

import numpy as np

row = 0
col = 0
array = []


if __name__ == "__main__":

  f = open('output_3.csv', 'r')
  lines = f.readlines()
  f.close();

  for line in lines:
#    line.replace(",.", ",0.");
    pattern = ",."
#    re.sub(pattern, " ", line)
    ta = line.rstrip().split(',')
    array.extend(ta)
    col = len(ta)
    row += 1

  array2 = np.array(array).reshape((row,col))
  #array3 = array2.astype(np.float)
  print row, col, array2
  #print row, col, array3[:,0]


