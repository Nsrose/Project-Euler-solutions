def triangleNum(n):
	result = 0
	for i in range(1, n+1):
		result +=i
	return result 

def listTriangles(start, end):
	listnum = []
	for i in range(start, end+1):
		if not isprime(triangleNum(i)) and triangleNum(i)%2==0:
			listnum.append(triangleNum(i))		
	return listnum

def lcf(n):
    for i in range(2, 1000000): #totally arbitrary endpoint in range so I don't crash my computer #
        if n%i ==0:
            return i

def isprime(n):
    if n == 2:
        return True 
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

def primefactors(n):
	factors = []
	lcf1 = lcf(n)
	next = n/lcf1
	if isprime(next):
	    return [lcf1, next]
	else:
	   	return [lcf1]+primefactors(next) 

def howmanytimes(n, nlist):
	total = 0
	for i in nlist:
		if i ==n:
			total +=1
	return total 

def numfactors(n):
	result = 1
	if isprime(n):
		return 2 
	listprimes = primefactors(n)
	newlist = []
	for i in listprimes:
		if i not in newlist:
			newlist.append(i) 
	for i in newlist:
		result *= howmanytimes(i, listprimes) + 1
	return result 

def answer(start, end):
	for i in listTriangles(start, end):
		if numfactors(i)>500:
			return i 

	