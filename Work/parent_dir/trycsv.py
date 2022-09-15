import csv

f = open('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4413598.csv', 'r')

for x in f:
	print(x)

f = open('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4413598.csv', 'r') 
lists_of_linestrings = csv.reader(f)

for x in lists_of_linestrings:
 	print(x)