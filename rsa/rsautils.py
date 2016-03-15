import sympy
from sympy.solvers.diophantine import extended_euclid

def modinv(a, m):
    y, x, g = extended_euclid(m, a)
    if g != 1:
        raise ValueError
    return x % m

def d_from_primes_e(primes, e):
    # Classic school book implementation
    # d = modinv(e, (r1-1)*(r2-1)*(rn-1)...)
    p_minus_1 = [p - 1 for p in primes]
    d = long(modinv(e, sympy.lcm_list(p_minus_1)))
    return d

def rsa_decrypt(ct, d, N):
    pt = pow(ct, d, N)
    return pt
