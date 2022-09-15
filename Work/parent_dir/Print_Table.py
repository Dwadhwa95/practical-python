import fileparse
import tableformat

def print_table(Portfolio, Attributes, formatter):

	formatter.headings(Attributes)

	for x in Portfolio:
		print("\n")
		for y in Attributes:	
			print(f'{getattr(x,y):^10}', end = " ")


portfolio = fileparse.read_portfolio('Data/portfolio.csv', types = [str, int, float])
formatter = tableformat.create_formatter('txt')
attributes = ['name', 'shares', 'price']
print_table(portfolio,attributes,formatter)




