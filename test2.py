listprimes = []
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

listprimes = filter(isprime, range(2,100))
listdiff = []
for i in range(0, len(listprimes)-1):
	listdiff.append(listprimes[i+1] - listprimes[i])
print listdiff