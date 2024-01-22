from math import *

def isSquare(a):
	for i in range(0, int(sqrt(a)) + 1):
		if i*i == a:
			return True
	return False

def	quadraticResidue(x, p):
	for i in range(1, p):
		squaredA = x + p*i
		if isSquare(squaredA):
			return int(sqrt(squaredA))


print(quadraticResidue(6, 29))

# => only valid solution is when x = 6 and therefore a² = 64 => a = 8 or -8
