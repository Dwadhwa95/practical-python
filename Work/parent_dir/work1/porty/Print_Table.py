from .import fileparse
from .import tableformat
from .import stock

portfolio = fileparse.read_portfolio('Data/portfolio.csv', types = [str, int, float])
formatter = tableformat.create_formatter('txt')
attributes = ['name', 'shares', 'price']
tableformat.print_table(portfolio,attributes,formatter)
	



