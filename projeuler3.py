def isPalindrome(n):
	n = str(n) 
	if len(n)<2:
		return True
	else:
		return n[0] == n[len(n)-1] and isPalindrome(n[1:len(n)-1])

def maximum(x,y):
	if x>y:
		return x
	return y 

listpal = []
def result():
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			if isPalindrome(i*j):
				listpal.append(i*j)
	return reduce(maximum, listpal)








