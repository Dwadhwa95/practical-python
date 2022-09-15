# report.py
#
# Exercise 2.4
from pprint import pprint
import csv
total = 0
def read_prices(filename):
    file = open(filename,'rt')
    dict_of_prices = {}
    for line in file:
    #next(file)
        row = line.split(',') 
        try:
            dict_of_prices[row[0]] = float(row[1])
        except IndexError as e:
            print("couldn't parse line", e)

    file.close()
    return dict_of_prices

a = read_prices('Data/prices.csv')
pprint(a)
#for x in a:
   # total = total + a[x]

print("total:", total)