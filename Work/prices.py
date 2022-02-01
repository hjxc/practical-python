# prices.py
#
# Exercise 2.6

import csv
import sys
from pprint import pprint

def read_prices(filename):
    portfolio = {}
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if len(row) == 0:
                continue
            else:
                portfolio[row[0]] = row[1]

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'work/Data/prices.csv'

data = read_prices(filename)
pprint(data)