from work1.porty import fileparse

from work1.porty import tableformat
from work1.porty import stock

portfolio = read_portfolio('Data/portfolio.csv', types = [str, int, float])
formatter = tableformat.create_formatter('txt')
attributes = ['name', 'shares', 'price']
tableformat.print_table(portfolio,attributes,formatter)
	



