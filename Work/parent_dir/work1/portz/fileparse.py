# reads a CSV into a list of dictionaries 
from pprint import pprint 	
import csv 
import stock
import temp
import logging 
log = logging.getLogger(__name__)
m = []
def stock_name(s):
	return s['name']

def read_portfolio(filename, columns_select = None, types = None, delimiter = ',', has_headers = True, silence_errors = False):
	global m
	with open(filename, 'rt') as file: #opens the file

		file = iter(file)	#makes file iterable
		list_of_stocks = []

		if not has_headers and columns_select:
			raise RuntimeError("Can't select columns if there aren't any headers")	
		
		if has_headers:		#checks if there are headers 
			
			headers = next(file)  #reads the header line
			headers = headers.strip()
			headers = headers.split(delimiter) #splits headers into a list - name,shares,price
			
		if columns_select:	#checks if the column_select operation is selected
				
			indexlist = [headers.index(x) for x in columns_select]
			headers_selected = [headers[a] for a in indexlist]	
			for i,line in enumerate(file,start=1):
				line = line.strip()
				line = list(line.split(delimiter))
				line_new = [line[a] for a in indexlist]    
				if types:                                                                                              
					try:
						line_new = [a(b) for a,b in zip(types,line_new)]					
					except ValueError as e:
						log.warning(f"Couldn't parse Row number {i}")
						log.debug(f'Reason : {e}')

						if silence_errors == True:
							continue		

				a = dict(zip(headers_selected,line_new))
				#for i,x in enumerate(headers_selected):
				#	a[f'{x}'] = line_new[i]				

				#a = stock.Stock()	

				list_of_stocks.append(a)
				m.append(a)

			list_of_stocks = [stock.Stock(**d) for d in list_of_stocks]
			x = temp.Portfolio()
			for a in list_of_stocks:
				x.append(a)



			

		else:	
			for line in file:    #iterates over each line in the file 
				if not line:
					print('missing data in line : ', lineno)
					continue
					
				line = line.strip()
				line = line.split(',')

				if types:
					try:
						line = [a(b) for a,b in zip(types,line)]

					except ValueError as e:
						print(e)
						if silence_errors == True:
							continue

				d = dict(zip(headers,line))	
				list_of_stocks.append(d)
				m.append(d)
	
			list_of_stocks = [stock.Stock(**d) for d in list_of_stocks]
			x = temp.Portfolio()
			for a in list_of_stocks:
				x.append(a)


	return x


def read_prices(filename,types = [str,float]):
	with open(filename, 'rt') as file:
		
		List_of_Prices = []

		for line in file:
			if not line:
				print('missing data')
				continue
			else:
				line = line.strip()
				line = line.split(',')
				try:
					if types:
						line_new = [a(b) for a,b in zip(types,line)]				
						line_new = stock.New_Price(line_new[0], line_new[1])
						List_of_Prices.append(line_new)
					else:
						line = stock.New_Price(line[0],line[1])
						List_of_Prices.append(line)		
				except IndexError as e:
					continue
				

	return List_of_Prices

if __name__ == '__main__':

	#logging.basicConfig()
	logging.basicConfig(filename = 'app.log',            # Name of the log file (omit to use stderr)
 	filemode = 'w',                  # File mode (use 'a' to append)
 	level    = logging.DEBUG)      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
	# logging.getLogger(__name__).level = logging.DEBUG
	opts = {'silence_errors': True, 'has_headers': True}
	a = read_portfolio('Data/missing.csv', columns_select = ['name', 'shares', 'price'], types = [str,int,float],**opts)
	b = read_prices('Data/prices.csv')

	# for x in a:
	# 	pprint(x)

	# a = list(a)	
	# pprint(a)
	# a.sort(key = lambda s: s.price)
	# for x in a:
	# 	print(x)

	#m.sort(key = lambda s: s['name'])
	#pprint(m)

	#for x in a:
	#	pprint(x)
	#pprint(a)
	#pprint(b)


