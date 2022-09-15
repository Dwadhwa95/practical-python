
from follow import follow 
import csv
import ticker

def countdown(n):

	print('Count down from ',n)
	while n>0:
		yield n
		n -= 1

def filematch(lines,substr):
	for line in lines:
		if substr in line:
			yield line

lines = follow('C:/users/Deepesh/downloads/practical-python/work/Data/stocklog.csv')

rows = csv.reader(lines)
for row in rows:
	print(row)

ibm = filematch(lines, 'IBM')
for line in ibm:
	print(line)



'''if __name__ == '__main__':
			
	y = countdown(10)
	#print(y)		
	for x in countdown(10):
		print(x)		'''


