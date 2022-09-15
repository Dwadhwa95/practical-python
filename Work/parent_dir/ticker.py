import csv
from follow import follow 

def generator(n):
	while n>0:
		n-=1
		yield f'{n}'

def select_columns(lines,index):
	for line in lines:
		yield [line[i] for i in index] 

def convert_types(lines,types):
	for line in lines: 
		yield[a(b) for a,b in zip(types,line)]

def make_dicts(lines,headers):
	for line in lines:
		yield dict(zip(headers,line))

def filter_symbols(rows, names):
        row = (row for row in rows if row['name'] in names)
        yield row


def parse_stock_data(lines, index, types, headers):

	rows = csv.reader(lines)
	rows = select_columns(rows,index)
	rows = convert_types(rows,types)
	rows = make_dicts(rows, headers)

	return rows 

if __name__ == '__main__':

	lines = follow('Data/stocklog.csv') 
	rows = parse_stock_data(lines,[0,1,4], [str, float, float], ['name', 'price', 'change'])

	for row in rows:
		print(row)


