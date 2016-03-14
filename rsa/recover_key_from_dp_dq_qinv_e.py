#!/bin/env/python2

from sympy import primetest
from generate_pem_from_pqe import generate_pem_from_pqe

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
                                print "\n\nP=%d\n\nQ=%d\n" % (p, q)
    return results

def generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e):
    pqe = recover_pqd_from_dp_dq_qinv_e(dp, dq, qinv, e)
    return generate_pem_from_pqe(*pqe[0])

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <dp> <dq> <qinv> <e>" % sys.argv[0]
    else:
        convert = lambda x: int(x, 16) if x[:2] == "0x" else int(x)
        args = [convert(x) for x in sys.argv[1:]]
        print generate_pem_from_dp_dq_qinv_e(*tuple(args))
