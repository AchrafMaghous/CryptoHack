# extendedGCD

def reverse_euclid_algo(p, q):
    if p == 0:
        return q, 0, 1
    gcd, x1, y1 = reverse_euclid_algo(q % p, p)

    x = y1 - (q // p) * x1
    y = x1
    
    return gcd, x, y

print(reverse_euclid_algo(26513, 32321))