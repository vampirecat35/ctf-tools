from sympy.solvers.diophantine import extended_euclid

def modinv(a, m):
    y, x, g = extended_euclid(m, a)
    print a, m, g, x, y
    if g != 1:
        raise ValueError
    return x % m
