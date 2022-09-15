
class TableFormatter:

	def headings(self,headers):
		raise NotImplementedError()

	def row(self,rowdata):
		raise NotImplementedError()

class TextTableFormatter(TableFormatter):
		
	def headings(self,headers): 		
		for h in headers:
			print(f'{h:^10s}', end = ' ')
		print()	
		print(('*'*10 + ' ')*len(headers))

	def row(self,rowdata):
		for i,x in enumerate(rowdata):
			print("\n")
			for y in rowdata[i]:	
				print(f'{y:^10}', end = " ")

class CSVTableFormatter(TableFormatter):
		
	def headings(self,headers):
		print(",".join(headers))

	def row(self,rowdata):
		a=0
		for i,x in enumerate(rowdata):
			rowdata[i] = [f'{x[a]:s}' , f'{x[a+1]:d}', f'{x[a+2]:0.2f}', f'{x[a+3]:0.2f}'] 

		for x in rowdata:
			print(",".join(x))		

class HTMLTableFormatter(TableFormatter):

	def headings(self,headers):
		print("<tr><th>" + "</th><th>".join(headers) + "</th></tr>")

	def row(self,rowdata):
		a=0
		for i,x in enumerate(rowdata):
			rowdata[i] = [f'{x[a]:s}' , f'{x[a+1]:d}', f'{x[a+2]:0.2f}', f'{x[a+3]:0.2f}'] 

		for x in rowdata:
			print("<tr><td>" + "</td><td>".join(x) + "</td></tr>")		

class FormatError(Exception):
	pass

def create_formatter(name):

	
	if name == 'txt':

		formatter = TextTableFormatter()

	elif name == 'csv':

		formatter = CSVTableFormatter()

	elif name == 'html':	

		formatter = HTMLTableFormatter()

	else:	
		raise FormatError('Invalid format type')

	return formatter


def print_table(Portfolio, Attributes, formatter):

	formatter.headings(Attributes)

	for x in Portfolio:
		print("\n")
		for y in Attributes:	
			print(f'{getattr(x,y):^10}', end = " ")
