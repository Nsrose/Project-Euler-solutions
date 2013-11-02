def fib(n):
	if n<1:
		return 1
	return fib(n-1) + fib(n-2)

n = 1
total = 0
while fib(n) <= 4000000:
	total += fib(n)
	n +=3 

print total 
