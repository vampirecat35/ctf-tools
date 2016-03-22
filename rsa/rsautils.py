from Crypto.Util import asn1
import sympy
from sympy import primetest
from sympy.solvers.diophantine import extended_euclid
from fractions import gcd
import random
from collections import namedtuple

PrivateKey = namedtuple('Key', ['N','e','d','p','q','dp','dq','qinv'])


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

# Based on https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/equation
def recover_pq_from_dp_dq_qinv_e(dp, dq, qinv, e):
    results = []
    d1p = dp * e - 1
    for k in range(3, e):
        if d1p % k == 0:
            hp = d1p // k
            p = hp + 1
            if primetest.isprime(p):
                d1q = dq * e - 1
                for m in range(3, e):
                    if d1q % m == 0:
                        hq = d1q // m
                        q = hq + 1
                        if primetest.isprime(q):
                            if (qinv * q) % p == 1 or (qinv * p) % q == 1:
                                results.append((p, q))
    return results


# Based on https://gist.github.com/ddddavidee/b34c2b67757a54ce75cb
def recover_pq_from_ned(n, e, d):
    """The following algorithm recovers the prime factors
        of a modulus, given the public and private
        exponents.
        Function call: recover_pq_from_ned(n, e, d)
        Input:     n: modulus
                e: public exponent
                d: private exponent
        Output: (p, q): prime factors of modulus"""

    def output_primes(a, n):
        p = gcd(a, n)
        q = int(n / p)
        if p > q:
            p, q = q, p
        return p,q

    k = d * e - 1
    if k % 2 == 1:
        return 0, 0
    else:
        t = 0
        r = k
        while(r % 2 == 0):
            r = int(r / 2)
            t += 1
        for i in range(1, 101):
            g = random.randint(0, n) # random g in [0, n-1]
            y = pow(g, r, n)
            if y == 1 or y == n - 1:
                continue
            else:
                for j in range(1, t): # j \in [1, t-1]
                    x = pow(y, 2, n)
                    if x == 1:
                        p, q = output_primes(y - 1, n)
                        return p, q
                    elif x == n - 1:
                        continue
                    y = x
                    x = pow(y, 2, n)
                    if  x == 1:
                        p, q = output_primes(y - 1, n)
                        return p, q


def generate_pem_from_key(key):
    seq = asn1.DerSequence()
    # key is in correct order
    seq[:] = [0] + list(key)
    exported_key = "-----BEGIN RSA PRIVATE KEY-----\n%s-----END RSA PRIVATE KEY-----" % seq.encode().encode("base64")
    return exported_key

def generate_key_from_pqe(p, q, e):
    N = p * q
    d = d_from_primes_e([p, q], e)
    dp = d % p
    dq = d % q
    qinv = pow(q, p - 2, p)

    return PrivateKey(N, e, d, p, q, dp, dq, qinv)

def generate_pem_from_pqe(p, q, e):
    key = generate_key_from_pqe(p, q, e)
    return generate_pem_from_key(key)

def generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e):
    results = recover_pq_from_dp_dq_qinv_e(dp, dq, qinv, e)
    assert len(results) > 0
    p = results[0][0]
    q = results[0][1]
    return generate_pem_from_pqe(p, q, e)

def rsa_decrypt(ct, d, N):
    pt = pow(ct, d, N)
    return pt

def rsa_encrypt(pt, e, N):
    ct = pow(pt, e, N)
    return ct
