from work1.porty import fileparse
import tableformat

portfolio = fileparse.read_portfolio('Data/portfolio.csv', types = [str, int, float])
formatter = tableformat.create_formatter('txt')
attributes = ['name', 'shares', 'price']
tableformat.print_table(portfolio,attributes,formatter)




