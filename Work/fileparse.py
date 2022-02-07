# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimeter=',', silence_errors=False):

    if select and not has_headers:
        raise RuntimeError('select requires column headers')
        
    rows = csv.reader(file, delimiter=delimeter)
    if has_headers:
        headers = next(rows)
    else:
        headers = []

    if select:
        indices = [headers.index(col) for col in select]
        headers = select


    records = []
    for i, row in enumerate(rows, 1):
        if not row:
            continue

        if select:
            row = [row[i] for i in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(e)
                continue
        
        if headers:
            record=dict(zip(headers,row))
        else:
            record = tuple(row)

        records.append(record)
    return records
