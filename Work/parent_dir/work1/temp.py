from porty import fileparse
import stock
class Portfolio:

	def __init__(self):

		self._holdings = []

	def __iter__(self):
		return self._holdings.__iter__()

	def __len__(self):
		return len(self._holdings)

	def __getitem__(self, index):
		return self._holdings[index]

	def __contains__(self, name):
		return any([s.name == name for s in self._holdings])

	@property
	def total_cost(self):
		
		return sum([s.shares*s.price for s in self._holdings])

	def append(self, holding):
		
		if not isinstance(holding, stock.Stock):
			raise TypeError('Expected a stock instance')
		self._holdings.append(holding)

	@classmethod
	def from_csv(cls, lines, **opts):
		self = cls()
		portdicts = fileparse

	def tabulate_shares():

		from collections import Counter
		total_shares = Counter()
		for s in self._holdings:
			total_shares[s.name] += s.shares 
		return total_shares


def add(x, y):
	def do_add():
		print('Adding', x, y)
		return x + y
	return do_add

a = add(5,7)
#print(a)