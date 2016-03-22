try:
    from pwn import hexdump
except ImportError:
    def hexdump(x): return x

from rsautils import *
from generate_pem_from_pqe import generate_key_from_pqe


def test():
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    import base64
    ct = base64.b64decode('R0vRTQQAafW+rjLu4+vd5FOtFRJJDFfk9R1bsilaMXZ/qaVb/P0gIHOWL9pHZembt17LPq+iyzYroUOnRoz3Bd/1svTAs9ucljfcZ7i65zpwyLfn2J+24KHtFssXRVOO/V0R/8DydJsFmjyhzvkzGx4Flr5XMREt+T/4ZeeNYTA=')
    p = 9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987245583
    q = 9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987246769
    e = 65537
    key = generate_key_from_pqe(p, q, e)
    ct = bytes_to_long(ct)
    pt = rsa_decrypt(ct, key.d, key.N)
    print hexdump(long_to_bytes(pt))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <p> <q> <e> <ct>" % sys.argv[0]
        print "       %s -test" % sys.argv[0]
    elif sys.argv[1] == "-test":
        test()
    else:
        convert = lambda x: int(x, 16) if x[:2] == "0x" else int(x)
        args = [convert(x) for x in sys.argv[1:]]
        key = generate_key_from_pqe(*tuple(args))
        pt = rsa_decrypt(ct, key['d'], key['N'])
        print hexdump(pt)
