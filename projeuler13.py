def collatzChain(n):
	if n == 1:
		return [n]
	elif n%2==0:
		return [n] + collatzChain(n/2)
	else:
		return [n] + collatzChain(3*n + 1) 

def maximum(x,y):
	if x>y:
		return x
	return y 

def answer():
	listlengths = []
	listis = []
	for i in range(999999, 10000, -2):
		listlengths.append(len(collatzChain(i)))
		listis.append(i) 
	return listis[listlengths.index(reduce(maximum, listlengths))] 