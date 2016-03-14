#!/bin/env/python2

from sympy import primetest

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
                                print(p, q)
    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <dp> <dq> <qinv> <e>" % sys.argv[0]
    else:
        dp   = int(sys.argv[1])
        dq   = int(sys.argv[2])
        qinv = int(sys.argv[3])
        e    = int(sys.argv[4])
        recover_pqd_from_dp_dq_qinv_e(dp, dq, qinv, e)
