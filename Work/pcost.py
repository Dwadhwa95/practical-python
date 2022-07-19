# pcost.py
#
# Exercise 1.27
total = 0
file = open('Data/portfolio.csv', 'rt')
next(file)
for line in file: 
	row = line.split(',')
	total = total + (int(row[1])*float(row[2]))

print(total)
file.close()
