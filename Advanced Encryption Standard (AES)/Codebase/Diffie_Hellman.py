import random
import time

def power(base, exponent, modulus=None):
    """
    Calculates base raised to the power of exponent, optionally modulo modulus.
    """
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
            if modulus is not None:
                result %= modulus
        base *= base
        if modulus is not None:
            base %= modulus
        exponent //= 2
    return result


def is_prime(n, k=5):
    """
    Miller-Rabin primality test.
    Returns True if n is probably prime, False otherwise.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = power(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_large_prime(k):
    while True:
        p = random.getrandbits(k) | (1 << k - 1) | 1  # Set the most significant and least significant bits to 1
        q = (p - 1) // 2  # q is a prime number if p is prime
        if is_prime(p) and is_prime(q):
            return p


def generate_primitive_root(p):
    gen = random.randint(2,p-1)
    while power(gen,2,p) == 1 or power(gen,(p-1)//2,p) == 1:
        gen = random.randint(2,p-1)
    return gen


