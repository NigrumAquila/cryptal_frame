from src.algorithms.SHA256 import SHA256
from src.constants.keyConstants import KEY_LENGTH_IN_BITS
from core.helpers.fileHelpers import pickFileFor
from core.math.multiplicativeInverse import multiplicativeInverse
from core.math.checkPrimesRelatively import checkPrimesRelatively
from core.math.findPrimitiveRoot import findPrimitiveRoot
from random import randint
from sympy import randprime


class EL_GAMAL_SIGNATURE_SCHEME():

    @staticmethod
    def generateKeys():
        p = randprime(2**(KEY_LENGTH_IN_BITS - 1), 2**KEY_LENGTH_IN_BITS)
        g = findPrimitiveRoot(p)
        x = randint(1, p-1); y = pow(g, x, p)
        privateKey = {'p': p, 'g': g, 'x': x}
        publicKey = {'p': p, 'g': g, 'y': y}
        return {'private': privateKey, 'public': publicKey}
        


    @staticmethod
    def sign(privateKey):
        srcFile, dstFile = pickFileFor('sign')
        hashValue = int(SHA256.digest(srcFile.read()).hex(), 16)
        
        k = randprime(1, privateKey['p'] - 1)
        while(checkPrimesRelatively(k, privateKey['p']) != True):
            k = randprime(1, privateKey['p'] - 1)
        r = pow(privateKey['g'], k, privateKey['p'])
        s = (multiplicativeInverse(k, privateKey['p'] - 1) * (hashValue - privateKey['x'] * r)) % (privateKey['p'] - 1)
        signature = {'r': r, 's': s}
        
        for param in signature:
            dstFile.write(param.encode() + ': '.encode() + str(hex(signature[param])[2:].upper()).encode() + '\n'.encode())
        srcFile.close(); dstFile.close()


    @staticmethod
    def verify(publicKey):
        srcFile, signFile = pickFileFor('verify')
        hashValue = int(SHA256.digest(srcFile.read()).hex(), 16)
        signature = {}
        for line in signFile.readlines():
            trim = line.decode().find(':') 
            key = line.decode()[:trim]
            signature[key] = int(line.decode()[trim+2:], 16)

        u1 = pow(publicKey['y'], signature['r'], publicKey['p'])
        u2 = pow(signature['r'], signature['s'], publicKey['p']) 
        lhs = u1 * u2 % publicKey['p']
        rhs = pow(publicKey['g'], hashValue, publicKey['p'])
        srcFile.close(); signFile.close()
        return lhs == rhs