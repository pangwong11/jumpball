#!/usr/bin/python

import argparse
from collections import defaultdict

debug = False

def parseArguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]',
                                     description='bd application')

    parser.add_argument('--debug', action='store_true', default=False)

    parser.add_argument('-m', '--min-area', dest='minArea', type=float, default=2.0,
                        help='specify the minimum area threshold')

    return parser.parse_args()

if __name__ == "__main__":

    config = defaultdict(list)
    args = parseArguments()
    debug = args.debug
