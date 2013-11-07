def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1) 

def add(x, y):
	return x+y 

def answer(n):
	number = str(factorial(n))
	listnum = []
	for i in range(0, len(number)):
		listnum.append(int(number[i])) 
	return reduce(add, listnum)
