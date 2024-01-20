# euclid algorithm

from math import gcd

def euclid_algo(a, b):
	if b == 0:
		return a
	else:
		return euclid_algo(b, a % b)

print("euclid_algo : ", euclid_algo(66528, 52920))

print("math.gcd: ", gcd(66528, 52920))

			
