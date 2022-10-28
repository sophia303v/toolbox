"""
  Read csv files in & write out using python standard library
"""

import csv

infile = "file"

data = []
with open(filename, newline='',encoding='utf-8') as f:
  for row in csv.reader(f):
     data.append(row)
  return row

with open(filename, 'w', newline='') as f:
  writer = csv.writer(f)
  for row in data:
    writer.writerow(row)

 
