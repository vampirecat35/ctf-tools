from Crypto.Util import asn1
import sympy
from sympy import primetest
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

# Stolen from https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/equation
def recover_pqd_from_dp_dq_qinv_e(dp, dq, qinv, e):
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
                                results.append((p, q, e))
    return results

def generate_pem_from_key(key):
    seq = asn1.DerSequence()
    seq[:] = [ 0, key['N'], key['e'], key['d'], key['p'], key['q'], key['dp'], key['dq'], key['qinv'] ]
    exported_key = "-----BEGIN RSA PRIVATE KEY-----\n%s-----END RSA PRIVATE KEY-----" % seq.encode().encode("base64")
    return exported_key

def generate_key_from_pqe(p, q, e):
    N = p * q
    d = d_from_primes_e([p, q], e)
    dp = d % p
    dq = d % q
    qinv = pow(q, p - 2, p)

    key = {}
    key['N'] = N
    key['e'] = e
    key['d'] = d
    key['p'] = p
    key['q'] = q
    key['dp'] = dp
    key['dq'] = dq
    key['qinv'] = qinv
    return key

def generate_pem_from_pqe(p, q, e):
    key = generate_key_from_pqe(p, q, e)
    return generate_pem_from_key(key)

def generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e):
    pqe = recover_pqd_from_dp_dq_qinv_e(dp, dq, qinv, e)
    return generate_pem_from_pqe(*pqe[0])

def rsa_decrypt(ct, d, N):
    pt = pow(ct, d, N)
    return pt
