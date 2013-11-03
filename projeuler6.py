minimum = 2
maximum = 2000

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

listprimes = []
while len(listprimes)<10000:
    listcand = range(minimum, maximum)
    for i in listcand:
        if isprime(i):
            listprimes.append(i)
    minimum = maximum
    maximum = minimum + 5000

print listprimes[10000]