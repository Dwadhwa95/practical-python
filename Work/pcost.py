# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):  					#calculates the total value of your portfolio by multiplying number of shares by price. 

	total = 0
	file = open(filename, 'rt') 				#opens the file
	headers = next(file)	
	print(headers)
	headers = headers.strip()
	print(headers)
	headers = headers.split(',')
	print(headers)			#returns a list of strings forming the first line in the file i.e the headers 							
	for lineno, line in enumerate(file, start=1):
		line = line.split(',')     			 #splits the line into a list of strings
		dict_of_prices = dict(zip(headers,line)) #forms a dictionary with headers as keys and list of strings as values
		try:
			number_of_shares = float(dict_of_prices['shares'])
			price = float(dict_of_prices['price'])	 
			total = total + (number_of_shares)*(price) 				#multiplies share price to share number and adds them to total 
		except ValueError:
			print("Missing data in line ", lineno, ". Continuing with the rest of the file and skipping:", line)

	file.close()	
	return total	

cost = portfolio_cost('Data/portfoliodate.csv')
print(cost)
