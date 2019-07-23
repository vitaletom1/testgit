import inspect 

def Tommy():
	pass

def squareit(x):
	return x * x

funcptr = squareit

setattr(Tommy, 'funcvar', funcptr)

for member in inspect.getmembers('Tommy'):
	print member
