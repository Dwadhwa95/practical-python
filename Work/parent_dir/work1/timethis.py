from time import time 

def timethis(func):
	def wrapper(*args, **argv):
		start = time()
		r = func(*args, **argv)
		end = time()
		print(f'{func.__name__} . {func.__module__}: {end-start}')
	return wrapper


