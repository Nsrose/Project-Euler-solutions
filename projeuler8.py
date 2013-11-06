def pythagTriplet(a, b, c):
	return a<b<c and a**2 + b**2 == c**2

def answer():
	for c in range(500, 80, -1):
		for b in range(c, 80, -1):
			for a in range(b, 80, -1):
				if pythagTriplet(a, b, c) and a + b+ c==1000:
					return a*b*c