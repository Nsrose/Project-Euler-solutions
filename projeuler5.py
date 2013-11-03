listnum = range(1, 101)

def add(x, y):
	return x +y
def square(x):
	return x**2

def sum_of_squares(listnum):
	return reduce(add, map(square, listnum))

def square_of_sum(listnum):
	return reduce(add, listnum)**2

print square_of_sum(range(1,101)) - sum_of_squares(range(1,101))