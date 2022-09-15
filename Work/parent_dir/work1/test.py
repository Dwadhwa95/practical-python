import fileparse
from timethis import timethis
#import simple
import unittest

# @property
# def shares(self):
# 	return self._shares

# @shares.setter	
# def shares(self,value):
# 	if not isinstance(value, int):
# 		raise TypeError('Expected an int')
# 	self._shares = value


def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

def add(x,y):
	return x+y


logged_add = logged(add)
a = logged_add(2,3)

@timethis
def countdown(n): 
	while n>0:
		n-=1


class TestAdd(unittest.TestCase):

	def test_simple(self):
		r = add(2,2)
		self.assertEqual(r,5)

	def test_str(self):
		r = add('hello', 'world')
		self.assertEqual(r, 'helloworld')


if __name__ == '__main__':
	
 	unittest.main()