file = open('Data/portfoliodate.csv', 'rt')
headers = next(file)
print(type(headers))
headers = headers.strip()
headers = headers.split(',')
print(headers)
print(type(headers))

select = ['name', 'shares', 'price']
index_list =[headers.index(x) for x in select]
print(index_list)

portfolio = []

for line in file:
	line.strip()
	line = line.split(',')
	portfolio.append({headers[a] : line[a].strip() for a in index_list})

print(portfolio)
#portfolio = []
#portfolio = portfolio.append({})