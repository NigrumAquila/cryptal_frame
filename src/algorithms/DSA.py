from src.algorithms.SHA256 import SHA256
from core.helpers.fileHelpers import pickFileFor
from core.math.multiplicativeInverse import multiplicativeInverse
from random import randint
from sympy import isprime


class DSA():

    N = 256
    L = 1024

    @staticmethod
    def __generate_p_q(L, N):
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
                    zzv = SHA256().digest(bin(arg).encode()).hex()
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


    @staticmethod
    def __generate_g(p, q):
        while True:
            h = randint(2, p - 1)
            exp = (p - 1) // q
            g = pow(h, exp, p)
            if g > 1:
                break
        return g

    @staticmethod
    def __generate_keys(g, p, q):
        x = randint(2, q)
        y = pow(g, x, p)
        return x, y

    @staticmethod
    def __generate_params(L, N):
        p, q = DSA.__generate_p_q(L, N)
        g = DSA.__generate_g(p, q)
        return p, q, g

    @staticmethod
    def __validate_params(p, q, g):
        if isprime(p) and isprime(q):
            return True
        if pow(g, q, p) == 1 and g > 1 and (p - 1) % q:
            return True
        return False

    
    @staticmethod
    def __validate_sign(r, s, q):
        if r < 0 and r > q:
            return False
        if s < 0 and s > q:
            return False
        return True


    @staticmethod
    def generateKeys():
        p, q, g = DSA.__generate_params(DSA.L, DSA.N)
        x, y = DSA.__generate_keys(g, p, q)
        privateKey = {'p': p, 'q': q, 'g': g, 'x': x}
        publicKey = {'p': p, 'q': q, 'g': g, 'y': y}
        return {'private': privateKey, 'public': publicKey}
        


    @staticmethod
    def sign(privateKey):
        if not DSA.__validate_params(privateKey['p'], privateKey['q'], privateKey['g']):
            raise Exception("Invalid params")

        srcFile, dstFile = pickFileFor('sign')
        hashValue = int(SHA256.digest(srcFile.read()).hex(), 16)
        
        k = randint(2, privateKey['q'])
        r = pow(privateKey['g'], k, privateKey['p']) % privateKey['q']
        s = (multiplicativeInverse(k, privateKey['q']) * (hashValue + privateKey['x'] * r)) % privateKey['q']
        signature = {'r': r, 's': s}
        
        for param in signature:
            dstFile.write(param.encode() + ': '.encode() + str(hex(signature[param])[2:].upper()).encode() + '\n'.encode())
        srcFile.close(); dstFile.close()


    @staticmethod
    def verify(publicKey):
        if not DSA.__validate_params(publicKey['p'], publicKey['q'], publicKey['g']):
            raise Exception("Invalid params")

        srcFile, signFile = pickFileFor('verify')
        hashValue = int(SHA256.digest(srcFile.read()).hex(), 16)
        signature = {}
        for line in signFile.readlines():
            trim = line.decode().find(':') 
            key = line.decode()[:trim]
            signature[key] = int(line.decode()[trim+2:], 16)

        if not DSA.__validate_sign(signature['r'], signature['s'], publicKey['q']):
            return False

        w = multiplicativeInverse(signature['s'], publicKey['q'])
        u1 = (hashValue * w) % publicKey['q']
        u2 = (signature['r'] * w) % publicKey['q']
        v = (pow(publicKey['g'], u1, publicKey['p']) * pow(publicKey['y'], u2, publicKey['p'])) % publicKey['p'] % publicKey['q']
        srcFile.close(); signFile.close()
        return v == signature['r']