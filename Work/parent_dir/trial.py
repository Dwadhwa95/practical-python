import stock

def read_portfolio(filename, columns_select = None, types = None, delimiter = ',', has_headers = True, silence_errors = False):
	with open(filename, 'rt') as file: #opens the file 
		
		file = iter(file)	#makes file iterable
		list_of_stocks = []

		if not has_headers and column_select:
			print("Can't select columns if there aren't any headers")	
		
		if has_headers:		#checks if there are headers 
			
			headers = next(file)  #reads the header line
			headers = headers.strip()
			headers = headers.split(delimiter) #splits headers into a list - name,shares,price
			
		if columns_select:	#checks if the column_select operation is selected
				indexlist = [headers.index(x) for x in columns_select]
				headers_selected = [headers[a] for a in indexlist]	
				for line in file:
					line = line.strip()
					line = list(line.split(','))
					line_new = [line[a] for a in indexlist]    
					if types:                                                                                              
						try:
							line_new = [a(b) for a,b in zip(types,line_new)]					
						except ValueError as e:
							print(e)		
							if silence_errors == True:
								continue
					a = stock.Stock([line_new[i] for i,x in enumerate(headers_selected)])			
					list_of_stocks.append(a)
							 			
		else:	
			for line in file:    #iterates over each line in the file 
				if not line:
					print('missing data in line : ', lineno)
					continue
					
				line = line.strip()
				line = line.split(delimiter)

				if types:
					try:
						line = [a(b) for a,b in zip(types,line)]
						print(line)

					except ValueError as e:
						print(e)
						if silence_errors == True:
							continue
					
				a = stock.Stock(line[0],line[1],line[2])
				list_of_stocks.append(a)

	
	return list_of_stocks


listofstocks = read_portfolio('Data/portfolio.csv',columns_select = None, types = [str,int,float], delimiter = ',', has_headers = True, silence_errors = True)