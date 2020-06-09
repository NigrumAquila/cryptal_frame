from random import randint
from src.common.multiplicativeInverse import multiplicativeInverse
from sympy import isprime
from src.algorithms.SHA256 import SHA256



def generate_p_q(L, N):
    g = N 
    n = (L - 1) // g
    b = (L - 1) % g
    while True:
        while True:
            s = randint(1, 2 ** (g))
            a = SHA256.digest(bin(s).encode()).hex()
            zz = (s + 1) % (2 ** g)
            z = SHA256.digest(bin(zz).encode()).hex()
            U = int(a, 16) ^ int(z, 16)
            mask = 2 ** (N - 1) + 1
            q = U | mask
            if isprime(q):
                break
        i = 0 
        j = 2 
        while i < 4096:
            V = []
            for k in range(n + 1):
                arg = (s + j + k) % (2 ** g)
                zzv = SHA256.digest(bin(arg).encode()).hex()
                V.append(int(zzv, 16))
            W = 0
            for qq in range(0, n):
                W += V[qq] * 2 ** (160 * qq)
            W += (V[n] % 2 ** b) * 2 ** (160 * n)
            X = W + 2 ** (L - 1)
            c = X % (2 * q)
            p = X - c + 1 
            if p >= 2 ** (L - 1):
                if isprime(p):
                    return p, q
            i += 1
            j += n + 1


def generate_g(p, q):
    while True:
        h = randint(2, p - 1)
        exp = (p - 1) // q
        g = pow(h, exp, p)
        if g > 1:
            break
    return g


def generate_keys(g, p, q):
    x = randint(2, q)
    y = pow(g, x, p)
    return x, y


def generate_params(L, N):
    p, q = generate_p_q(L, N)
    g = generate_g(p, q)
    return p, q, g






def validate_params(p, q, g):
    if isprime(p) and isprime(q):
        return True
    if pow(g, q, p) == 1 and g > 1 and (p - 1) % q:
        return True
    return False


def validate_sign(r, s, q):
    if r < 0 and r > q:
        return False
    if s < 0 and s > q:
        return False
    return True

class DSA():
    N = 256
    L = 1024

    @staticmethod
    def generateKey():
        p, q, g = generate_params(L, N)
        x, y = generate_keys(g, p, q)


    @staticmethod
    def sign(privateKey):
        if not validate_params(p, q, g):
        raise Exception("Invalid params")
        while True:
            k = randint(2, q)
            r = pow(g, k, p) % q
            m = int(SHA256.digest(M).hex(), 16)
            try:
                s = (multiplicativeInverse(k, q) * (m + x * r)) % q
                return r, s
            except ZeroDivisionError:

    
    @staticmethod
    def verify(publicKey):
        if not validate_params(p, q, g):
            raise Exception("Invalid params")
        if not validate_sign(r, s, q):
            return False
        try:
            w = multiplicativeInverse(s, q)
        except ZeroDivisionError:
            return False
        m = int(SHA256.digest(M).hex(), 16)
        u1 = (m * w) % q
        u2 = (r * w) % q
        v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
        if v == r:
            return True
        return False


if __name__ == "__main__":
    N = 256
    L = 1024
    p, q, g = generate_params(L, N)
    x, y = generate_keys(g, p, q)

    text = open('tasks', 'r').read()
    M = text.encode()
    r, s = sign(M, p, q, g, x)
    if verify(M, r, s, p, q, g, y):
        print('All ok')
        print(M)
        print(r)
        print(s)
        print(p)
        print(q)
        print(g)
        print(y)
        print(x)