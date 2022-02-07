# pcost.py
#
# Exercise 1.27

import csv
import sys
from fileparse import parse_csv

def portfolio_cost(filename):
    cost = 0
    with open(filename) as file:
        data = parse_csv(file,['shares', 'price'], [int, float], True)
    for row in data:
        cost += row['shares'] * row['price']

    return cost

def main():

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost {cost:.2f}')

if __name__ == '__main__':
    main()