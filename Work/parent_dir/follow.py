import os 
import time
import sys
sys.path.insert(0, 'C:/Users/Deepesh/downloads/practical-python/work')
import fileparse	              
import ticker

def follow(filename):

	f = open(filename)
	f.seek(0, os.SEEK_END)

	while True:
	    line1 = f.readline()
	    if line1 == '':
	        time.sleep(0.1)   # Sleep briefly and retry
	        continue
	    line = line1.split(',')
	    name = line[0].strip('"')
	    price = float(line[1])
	    change = float(line[4])
	    if change != 0:
	        yield line1


if __name__ == '__main__':

	Portfolio = fileparse.read_portfolio('C:/Users/Deepesh/downloads/practical-python/work/Data/portfolio.csv', columns_select = ['name', 'shares', 'price'] , types = [str, int, float], delimiter = ',', has_headers = True, silence_errors = False)
	lines = follow('C:/Users/Deepesh/downloads/practical-python/work/Data/stocklog.csv')
	lines = ticker.parse_stock_data(lines,[0,1,4], [str, float, float], ['name', 'price', 'change'])
	rows = ticker.filter_symbols(lines, [x.name for x in Portfolio])
	