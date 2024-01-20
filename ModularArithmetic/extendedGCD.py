# extendedGCD

def reverse_euclid_algo(p, q):
    if p == 0:
        return q, 0, 1
    
    # Recursive call to reverse_euclid_algo with updated parameters
    gcd, x1, y1 = reverse_euclid_algo(q % p, p)

    # Calculating the values of x and y using the extended Euclidean algorithm
    x = y1 - (q // p) * x1
    y = x1
    
    return gcd, x, y

print("u, v: ", reverse_euclid_algo(26513, 32321))