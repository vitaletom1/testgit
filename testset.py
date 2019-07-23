import inspect 

class Tommy():
	pass

def squareit(self, x):
	return x * x

funcptr = squareit

setattr(Tommy, 'funcvar', funcptr)

for member in inspect.getmembers(Tommy):
	print member

x = Tommy()

print x.funcvar(21)

