import random
import Diffie_Hellman as df

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):

    #Computes the extended GCD of two numbers.Returns a tuple (g, x, y) ,
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    # g is the GCD of a and b, and x, y are the coefficients satisfying the equation ax + by = g.


def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        # Set the two most significant bits to ensure a number with the desired number of bits
        n |= (1 << (bits - 1)) | 1
        if df.is_prime(n):
            return n


def generate_keys(bits):
    # Generate two large prime numbers p and q
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    # Compute n = p * q
    n = p * q

    # Compute phi(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent e
    e = random.randint(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)

    # Compute the modular multiplicative inverse of e modulo phi(n)
    _, d, _ = extended_gcd(e, phi_n)
    d %= phi_n

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def encrypt(message, public_key):
    e, n = public_key
    ciphertext = [df.power(ord(char), e, n) for char in message]
    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key
    message = ''.join([chr(df.power(char, d, n)) for char in ciphertext])
    return message




