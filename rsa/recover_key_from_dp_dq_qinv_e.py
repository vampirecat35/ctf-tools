#!/bin/env/python2

from sympy import primetest
from rsautils import *

def test1():
    dp   = 11188888442779478492506783674852186314949555636014740182307607993518479864690065244102864238986781155531033697982611187514703037389481147794554444962262361
    dq   = 1006725509429627901220283238134032802363853505667837273574181077068133214344166038422298631614477333564791953596600001816371928482096290600710984197710579
    qinv = 11196804284042107547423407831525890933636414684075355664222816007929037065463409676450144484947842399975707117057331864113464711778199061912128258484839473
    e    = 0x10001
    print generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e)

def test2():
    import base64
    from Crypto.Util.number import bytes_to_long
    key_suffix_b64 = '''
MGQCAQACEQDkIlffRGfwBX0cA2BJnB9/AgMBAAECEBExUWP/GMIq00yk9QZaDxEC
CQDzzjPYDtlExwIJAO+LelY/RCeJAgkA0nzzS5S+Rd8CCQDfayKmMInbqQIJAI8L
5/sTaOow
    '''.replace('\n','').replace(' ', '')

    # Assumptions about the key
    key_length = 128
    e          = 0x10001

    key_suffix = base64.b64decode(key_suffix_b64)

    qinv = bytes_to_long(key_suffix[-(key_length/2/8+1):])
    dq   = bytes_to_long(key_suffix[-(key_length/2/8+1)*2-2:-(key_length/2/8+1)-2])
    dp   = bytes_to_long(key_suffix[-(key_length/2/8+1)*3-4:-(key_length/2/8+1)*2-4])

    print generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e)

def test3():
    import base64
    from Crypto.Util.number import bytes_to_long
    key_suffix_b64 = '''
        Os9mhOQRdqW2cwVrnNI72DLcAXpXUJ1HGwJBANWiJcDUGxZpnERxVw7s0913WXNt
        V4GqdxCzG0pG5EHThtoTRbyX0aqRP4U/hQ9tRoSoDmBn+3HPITsnbCy67VkCQBM4
        xZPTtUKM6Xi+16VTUnFVs9E4rqwIQCDAxn9UuVMBXlX2Cl0xOGUF4C5hItrX2woF
        7LVS5EizR63CyRcPovMCQQDVyNbcWD7N88MhZjujKuSrHJot7WcCaRmTGEIJ6TkU
        8NWt9BVjR4jVkZ2EqNd0KZWdQPukeynPcLlDEkIXyaQx
    '''.replace('\n','').replace(' ', '')

    # Assumptions about the key
    key_length = 1024
    e          = 0x10001

    key_suffix = base64.b64decode(key_suffix_b64)

    qinv = bytes_to_long(key_suffix[-(key_length/2/8):])
    dq   = bytes_to_long(key_suffix[-(key_length/2/8)*2-3:-(key_length/2/8)-3])
    dp   = bytes_to_long(key_suffix[-(key_length/2/8)*3-6:-(key_length/2/8)*2-5])

    print generate_pem_from_dp_dq_qinv_e(dp, dq, qinv, e)




if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Usage: %s <dp> <dq> <qinv> <e>" % sys.argv[0]
        print "       %s -test1" % sys.argv[0]
        print "       %s -test2" % sys.argv[0]
    elif sys.argv[1] == '-test1':
        test1()
    elif sys.argv[1] == '-test2':
        test2()
    else:
        convert = lambda x: int(x, 16) if x[:2] == "0x" else int(x)
        args = [convert(x) for x in sys.argv[1:]]
        print generate_pem_from_dp_dq_qinv_e(*tuple(args))
