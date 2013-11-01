def foobarsum(n):
	total = 0
	for i in range(3, n):
		if i%3 == 0 or i%5 ==0:
			total +=i
	return total 
