# Useful tools for working with RSA cryptos

- `generate_pem_from_pqe.py`: If you have `p`, `q`, and `e`, this tool will generate a complete PEM file, containing `d`, `dp`, `dq`, `qinv`.
- `multiprime-decrypt.py`: If the public key factors to 3 primes, this tool can be used to decrypt the message.
- `recover_pq_from_dp_dq_qinv_e.py`: If you have a partial private key, such as the end of a PEM file, this tool will recover `p` and `q`, and you will be able to generate a complete PEM file with this.

# Useful openssl commands

Openssl can be a bit cryptic to use, no pun intended. Here are some useful commands when working with RSA crypto.

Generate a public key from a private PEM file:

    openssl rsa -in private.pem -pubout > public.pem

Encrypting a message with a public key: (Note that the message can't be longer than the key size)

    cat plaintext.txt | openssl rsautl -encrypt -pubin -inkey public.pem > ciphertext.txt

Decrypting a ciphertext with a complete private key in PEM format:

    cat ciphertext.txt | openssl rsautl -decrypt -inkey private.pem
