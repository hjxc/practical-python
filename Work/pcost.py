# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    cost = 0
    record = {}
    with open(filename) as file:
        data = csv.reader(file)
        headers = next(data)
        for i, row in enumerate(data):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                cost += shares * price
            except ValueError:
                print(f'could not parse row {i}: {row}')

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')