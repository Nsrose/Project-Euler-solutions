# WARNING: This program takes up 100% of my CPU on my Macbook Pro Retina and runs for about 1 minute. #

minimum = 2000
maximum = 20000


candidates = range(minimum, maximum)
def isdivisible(n):
	return n%2==n%3==n%4==n%5==n%7==n%8==n%9==n%10==n%11==n%12==n%13==n%14==n%16==n%17==n%19==n%20==0

numbers = []
while numbers == []:
	candidates = range(minimum, maximum)
	numbers = filter(isdivisible, candidates)
	minimum = maximum
	maximum = 20000+minimum

print numbers 