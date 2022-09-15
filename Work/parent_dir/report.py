# report.py
#
# Exercise 2.4

import stock
from pprint import pprint 
total = 0
def read_portfolio(filename):
	with open(filename,'rt') as file:
		headers = next(file)
		headers = headers.strip()
		headers = headers.split(',')
		for line in file:
			line = line.strip()
			line = line.split(',')
			entry = Stock(line[0],line[1],line[2])
			list_of_stocks.append(entry)
	
	return list_of_stocks


def read_prices(filename):

	with open(filename,'rt') as file: 
		dict_of_prices = {}
		for line in file:

			row = line.strip()
			row = line.split(',') 
			if len(row) == 2:
				dict_of_prices[row[0]]   = float(row[1])
			else:
				print("couldn't parse line", row)
		
	return dict_of_prices


Price_List_New = read_prices('Data/prices.csv')
Portfolio_Old = read_portfolio('Data/portfolio.csv')

for x in Portfolio_Old:
	print(type(x['shares']), type(x['price']))

Total_Old = sum(float(x['shares'])*float(x['price']) for x in Portfolio_Old)
Total_New = sum(float(x['shares'])*float(Price_List_New[x['name']]) for x in Portfolio_Old) 
print("Loss/Gain on Portfolio = ", Total_New - Total_Old )

for x in Portfolio_Old:
	Loss_Gain = float(x['shares'])*float(Price_List_New[x['name']]) - float(x['shares'])*float(x['price']) 
	print("Gain/Loss on", x['name'], "is ", Loss_Gain)


#Total_Portfolio = sum(float(x['shares'])*float(x['price']) for x in b)
#print("Total value:", Total_Portfolio)
 











































