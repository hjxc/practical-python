# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv

def portfolio_cost(filename):
    with open(filename) as file:
        portfolio = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio

def read_prices(filename):
    with open(filename) as file:
        prices = parse_csv(file, types=[str, float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        name = row['name']
        diff = prices[name] - row['price']
        stock = (name, row['shares'], prices[name], diff)
        report.append(stock)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def main():
    if len(sys.argv) == 3:
        price_filename = sys.argv[1]
        portfolio_filename = sys.argv[2]
    else:
        price_filename = 'work/Data/prices.csv'
        portfolio_filename = 'work/Data/portfolio.csv'
    prices = read_prices(price_filename)
    portfolio = portfolio_cost(portfolio_filename)
    report = make_report(portfolio, prices)
    print_report(report)

if __name__ == '__main__':
    main()

