'''def typedproperty(name, expected_type):

	private_name = '_' + name
	
	@property
	def prop(self):
		return getattr(self, private_name)

	@prop.setter
	def prop(self,value)
		if not isinstance(value, expected_type):
			raise TypeError(f'Expected{expected_type}')
		setattr(self,private_name,value)

	return prop '''


from pprint import pprint 
import typedproperty 

class Stock(object): 

	#__slots__ = ('name', '_shares', 'price')

	name = typedproperty.String('name')
	shares = typedproperty.Integer('shares')
	price = typedproperty.Float('price')
	

	def __init__(self, name, shares, price):
		
		self.name = name 
		self.shares = shares
		self.price = price
	
	def sell(self, number_to_sell):
		self.shares -= number_to_sell
		print( number_to_sell, 'share sold at', self.price )
		return self.shares
 
	@property
	def cost(self):
		value = self.price*self.shares
		return value

	def __repr__(self):
		return f'Stock({self.name} , {self.shares}, {self.price})'

	

class MyStock(Stock):

	def __init__(self, name, shares, price, factor):
		super().__init__(name, shares, price)
		self.factor = factor

	def panic(self):
		self.sell(self.shares)
		
	def cost(self):
		actual_cost = super().cost()
		return self.factor* actual_cost           

class NewStock(Stock):
	pass                                                

class New_Price:

	def __init__(self,name,price):

		self.name = name 
		self.price = price


if __name__ == '__main__':
		
		goog = Stock('GOOG',100,490.1)
		goog.sell(6)

		

