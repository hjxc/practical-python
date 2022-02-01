# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def portfolio_cost(filename):
    cost = 0
    portfolio = []

    with open(filename) as file:
        data = csv.reader(file)
        headers = next(data)
            

        for row in data:
            new_row = (row[0], int(row[1]), float(row[2]))
            record = dict(zip(headers, row))
            print(record)
            # portfolio.append({'name': row[0], 'shares': int(row[1]), 'price':float(row[2])})
            portfolio.append(record)

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if len(row) == 0:
                continue
            else:
                prices[row[0]] = float(row[1])

    return prices

def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        name = row['name']
        diff = prices[name] - row['price']
        stock = (name, row['shares'], prices[name], diff)
        report.append(stock)
    return report

prices = read_prices('work/Data/prices.csv')
portfolio = portfolio_cost('work/Data/portfolio.csv')

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)