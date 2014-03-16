#!/usr/bin/python


import urllib2
import urllib
import argparse
from bs4 import BeautifulSoup
import csv 
import glob

# Create file out.txt
f = csv.writer(open('out.txt', 'w+'))

# Iterate over all the files from the data source website
for num in xrange(0, 10000):
  number = '{0:04}'.format(num) 
 # page = urllib2.urlopen("http://cs1.calstatela.edu/~jtran/graphs/%s" % number)
  urllib.urlretrieve("http://cs1.calstatela.edu/~jtran/graphs/%s" % number, "./graph_data_files/%s" % number)
  
  # Combine all fines and write to out.txt
#  read_files = glob.glob("./graph_data_files/%s" % number)
#  with open("out.txt", "wb") as outfile:
#    for f in read_files:
#      with open(f, "rb") as infile:
#        outfile.write(infile.read())


