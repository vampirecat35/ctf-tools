from rsautils import *

def test():
    # For testing

    N =    0xE42257DF4467F0057D1C0360499C1F7F
    e =    0x10001
    d =    0x11315163FF18C22AD34CA4F5065A0F11
    p =    0xF3CE33D80ED944C7
    q =    0xEF8B7A563F442789
    dp =   0xD27CF34B94BE45DF
    dq =   0xDF6B22A63089DBA9
    qinv = 0x8F0BE7FB1368EA30
    print  generate_pem_from_pqe(p, q, e)

    '''
    Should generate a key that, when viewed with asn1parse, generates the following output:
     0:d=0  hl=2 l= 100 cons: SEQUENCE
     2:d=1  hl=2 l=   1 prim:  INTEGER           :00
     5:d=1  hl=2 l=  17 prim:  INTEGER           :E42257DF4467F0057D1C0360499C1F7F
    24:d=1  hl=2 l=   3 prim:  INTEGER           :010001
    29:d=1  hl=2 l=  16 prim:  INTEGER           :11315163FF18C22AD34CA4F5065A0F11
    47:d=1  hl=2 l=   9 prim:  INTEGER           :F3CE33D80ED944C7
    58:d=1  hl=2 l=   9 prim:  INTEGER           :EF8B7A563F442789
    69:d=1  hl=2 l=   9 prim:  INTEGER           :D27CF34B94BE45DF
    80:d=1  hl=2 l=   9 prim:  INTEGER           :DF6B22A63089DBA9
    91:d=1  hl=2 l=   9 prim:  INTEGER           :8F0BE7FB1368EA30
    '''

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <p> <q> <e>" % sys.argv[0]
    elif sys.argv[1] == '-test':
        test()
    else:
        convert = lambda x: int(x, 16) if x[:2] == "0x" else int(x)
        args = [convert(x) for x in sys.argv[1:]]
        key = generate_key_from_pqe(*tuple(args))
        pem = generate_pem_from_key(key)
        print key
        print pem
