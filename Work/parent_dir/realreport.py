import fileparse
import tableformat
import sys

def Fetch_Report_Data(portfolio,prices):

	Change_Data = []
	for x in portfolio:
		for y in prices: 
			if x.name == y.name:
				Loss_Gain = float(y.price) - float(x.price)
				Change_Data.append([x.name, x.shares, x.price, Loss_Gain])
				break
			else:
				continue
	
	return Change_Data


def Fetch_portfolio_and_prices(portfoliofile, pricesfile, fmt ):

    portfolio = fileparse.read_portfolio(portfoliofile, columns_select = ['name', 'shares', 'price'], types = [str,int,float], delimiter = ',', has_headers = True, silence_errors = True)
    prices = fileparse.read_prices(pricesfile)
    
    return (portfolio,prices)

    
def print_report(Change_Data,formatter):

	formatter.headings(['Name','Shares','Price','Change'])

	formatter.row(Change_Data)

if __name__ == '__main__':

	portfolio_and_prices = Fetch_portfolio_and_prices('Data/portfolio.csv','Data/prices.csv', 'txt')
	report_data = Fetch_Report_Data(*portfolio_and_prices)
	try:
		formatter = tableformat.create_formatter('txt')
	except FormatError as e:
		print('Please enter correct format')
 		   
	print_report(report_data,formatter)