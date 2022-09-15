file = open('Data/portfolio.csv', 'rt')
types = [str, int, float]

headers = next(file).strip()
headers = headers.split(',')
print(headers)
r=[]

from pprint import pprint 
for line in file: 
	line = line.strip()
	line = line.split(',')
	r.append(list(zip(types,line)))
converted = []
for x in r:
   	converted.append([(func,func(value)) for func,value in x])

pprint(converted)

List_of_Dict = []
for x in converted: 
	List_of_Dict.append({headers[i]: t[1] for i,t in enumerate(x)})
		
pprint(List_of_Dict)

price_tuple = []
for x in converted:
	price_tuple.append(list(i[1] for i in x))

pprint(price_tuple)
