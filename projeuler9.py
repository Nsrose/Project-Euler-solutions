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


def answer():
    total = 0 
    for i in range(2, 2000000):
        if isprime(i):
            total += i
    return total 