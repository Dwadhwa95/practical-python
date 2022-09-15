import fileparse
import stock
import tableformat

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


def print_report(Change_Data,formatter):

	formatter.headings(['Name','Shares','Price','Change'])

	formatter.row(Change_Data)


