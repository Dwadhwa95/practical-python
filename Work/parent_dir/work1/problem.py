import fileparse
import realreport 
from tableformat import FormatError
import tableformat 
import stock
import csv
from pprint import pprint 


def portfolio_report(portfoliofile, pricesfile, fmt ):

    portfolio = fileparse.read_portfolio(portfoliofile, columns_select = ['name', 'shares', 'price'], types = [str,int,float], delimiter = ',', has_headers = True, silence_errors = True)
    prices = fileparse.read_prices(pricesfile)
    report_data = realreport.Fetch_Report_Data(portfolio,prices)
    try:
        formatter = tableformat.create_formatter(fmt)
    except FormatError as e:
        print('Please enter correct format')

    realreport.print_report(report_data,formatter)


def main(argv):

    portfolio_report(argv[1],argv[2],argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)


#Formatter.headings(['Name', 'Shares', 'Price','Change'])
    #headers_report = ['Name', 'Shares', 'Price', 'Change']   
    #for name, shares, price, change in Report_Data:
     #   rowdata = [name, shares, f'{price:0.2f}', f'{change:0.2f}'] 
    #Formatter.row(rowdata)

#print("\n")
#a = globals()
#pprint(a)
#print("\n")
#pprint(stock.Stock.__dict__)
