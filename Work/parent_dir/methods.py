class Date(object):	
	
	def __init__(self,year,month,day):
		
		self.year = year
		self.month = month
		self.day = day

	def __str__(self):
		return f"{self.year}-{self.month}-{self.day}"

	def __repr__(self):
		return f"Date({self.year},{self.month},{self.day})"


a = Date(2012,12,12)
b = a.__str__()
c = a.__repr__()
z = eval(c)

print(a)
print(b)
print(c)
print(z)
print(abs(3.145))
		