# report.py
#
# Exercise 2.4
from pprint import pprint
import csv
total = 0
def dictionary_portfolio(filename):
	with open(filename) as file:
		listofdict = []
		headers = next(file)
		headers = headers.split(',')
		for line in file:
			row = line.split(',')
			listofdict.append({headers[0]:row[0], headers[1]:row[1], headers[2]:row[2]})

	return listofdict


def read_prices(filename):

	with open(filename,'rt') as file: 
		dict_of_prices = {}
		for line in file:
	#next(file)				
			row = line.split(',') 
			if len(row) == 2:
				#try:
				dict_of_prices[row[0]]   = float(row[1])
				#except ValueError: 
			else:
				print("couldn't parse line", row)
		
	return dict_of_prices

#def make_report(listofdict, dictofprices): 
	
	#print(f'{'':^10s} {'Shares':^10d} {'Price Change': ^10.2f}')

a = read_prices('Data/prices.csv')
keys = a.keys()
keys = list(keys)
#for x in keys:
	#total = total + float(a[x])	

#print("total:", total)
b = dictionary_portfolio('Data/portfolio.csv')
i = 0
total_old = 0
total_new = 0
for i,x in enumerate(b, start=0): 
	keys1 = list(b[i].keys())
	total_new = total_new + (float(a[b[i][keys1[0]]])*float(b[i][keys1[1]]))
	total_old = total_old + (float(b[i][keys1[1]])*float(b[i][keys1[2]]))
	gain_loss = (float(a[b[i][keys1[0]]])*float(b[i][keys1[1]])) - (float(b[i][keys1[1]])*float(b[i][keys1[2]]))
	print('gain/loss on ', b[i][keys1[0]], 'is', gain_loss) 


print('total portfolio value old: ', total_old, '\ntotal new value : ', total_new )
print('total gain/loss = ', total_new - total_old)