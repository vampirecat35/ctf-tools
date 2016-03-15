#!/bin/env/python2

from sympy import primetest
from rsautils import *

def test():
    dp   = 11188888442779478492506783674852186314949555636014740182307607993518479864690065244102864238986781155531033697982611187514703037389481147794554444962262361
    dq   = 1006725509429627901220283238134032802363853505667837273574181077068133214344166038422298631614477333564791953596600001816371928482096290600710984197710579
    qinv = 11196804284042107547423407831525890933636414684075355664222816007929037065463409676450144484947842399975707117057331864113464711778199061912128258484839473
    e    = 0x10001
    print generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <dp> <dq> <qinv> <e>" % sys.argv[0]
        print "       %s -test" % sys.argv[0]
    elif sys.argv[1] == '-test':
        test()
    else:
        convert = lambda x: int(x, 16) if x[:2] == "0x" else int(x)
        args = [convert(x) for x in sys.argv[1:]]
        print generate_pem_from_dp_dq_qinv_e(*tuple(args))
