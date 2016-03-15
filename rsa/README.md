# Useful tools for working with RSA cryptos

- [generate_pem_from_pqe](./generate_pem_from_pqe.py): If you have `p`, `q`, and `e`, this tool will generate a complete PEM file, containing `N`, `d`, `dp`, `dq`, `qinv`.
- [multiprime_decrypt](multiprime_decrypt.py): If the public key/modulo/`N` factors to 3 primes, this tool can be used to decrypt the message. It can easily be modified to support more than 3 primes.
- [recover_key_from_dp_dq_qinv_e.py](recover_pq_from_dp_dq_qinv_e.py): If you have a partial private key, such as the end of a PEM file, this tool will recover `p` and `q`, and then generate a complete private key in PEM format.
- [rsa_decrypt](rsa_decrypt.py): Decrypts a ciphertext with known `p`, `q`, `e` and of course a `ciphertext`.

# Useful openssl commands

Openssl can be a bit cryptic to use, no pun intended. Here are some useful commands when working with RSA crypto.

Generate a public key from a private key in PEM format:

    openssl rsa -in private.pem -pubout > public.pem

Encrypting a message with a public key: (Note that the message can't be longer than the key length)

    cat plaintext.txt | openssl rsautl -encrypt -pubin -inkey public.pem > ciphertext.txt

Decrypting a ciphertext with a complete private key in PEM format:

    cat ciphertext.txt | openssl rsautl -decrypt -inkey private.pem
