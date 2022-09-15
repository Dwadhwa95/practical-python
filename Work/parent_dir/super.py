import stock
from pprint import pprint

class A:
	pass

class B(A):
	pass 

class C(stock.Stock,B):
	pass

'''print(C.__bases__)

print(type(C))
x = A()
print(type(x))

a = C.__mro__
print(a)
'''

class Loudsuper:
	def noise(self):
		return 'loudsuper executed'


class Dog:
	def noise(self):
		return 'Bark'

	def chase(self):
		return 'Chasing!'

class Bike:

	def noise(self):
		return 'On your left'

	def pedal(self):
		return 'Pedaling!'


class Loud:
	def noise(self):
		return super().noise().upper()

class LoudDog(Loud,Dog):
	pass

class LoudBike(Loud,Bike):	
	pass

pprint(LoudDog.__mro__)

#y = Loud()
#b = y.noise()
	
x = LoudDog()
a = x.noise()
print(a)
