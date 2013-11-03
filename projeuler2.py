import math
number = input("Enter number you want factored: ")

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

# Least common factor needs optimization desperately #
def lcf(n):
    for i in range(2, 1000000): #totally arbitrary endpoint in range so I don't crash my computer #
        if n%i ==0:
            return i
listnum = []
def primefactors(n):
    lcf1 = lcf(n)
    next = n/lcf1
    if isprime(next):
        return [lcf1, next]
    else:
        return [lcf1]+primefactors(next) 
print primefactors(number) 
