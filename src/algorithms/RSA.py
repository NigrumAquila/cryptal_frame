from ..common.checkPrimesRelatively import checkPrimesRelatively
from ..common.multiplicativeInverse import multiplicativeInverse
from ..helpers.fileHelpers import pickFileFor
from ..helpers.constants import KEY_LENGTH_IN_BITS, KEY_LENGTH_IN_BYTES
from sympy import randprime


class RSA:
    @staticmethod
    def generateKeys():
        p = randprime(2**(KEY_LENGTH_IN_BITS/2-1), 2**(KEY_LENGTH_IN_BITS/2)) 
        q = randprime(2**(KEY_LENGTH_IN_BITS/2-1), 2**(KEY_LENGTH_IN_BITS/2))
        n = p*q; fi = (p-1)*(q-1)
        e = randprime(1, fi)
        while(checkPrimesRelatively(e, fi) != True):
            e = randprime(1, fi)
        d = multiplicativeInverse(e, fi)
        publicKey = {'e': e, 'n': n}; privateKey = {'d': d, 'n': n}
        return {'public': publicKey, 'private': privateKey}


    @staticmethod
    def encrypt(publicKey):
        from progress.bar import Bar

        srcFile, dstFile = pickFileFor('encrypt')
        
        with Bar('Processing', max=len(srcFile.read())) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(1)
                if not char: break
                cipherChar = pow(int.from_bytes(char, byteorder='big'), publicKey['e'], publicKey['n'])
                cipherBytes = cipherChar.to_bytes(KEY_LENGTH_IN_BYTES, byteorder='big')
                dstFile.write(cipherBytes)
                bar.next()
        srcFile.close(); dstFile.close()


    @staticmethod
    def decrypt(privateKey):
        from progress.bar import Bar

        srcFile, dstFile = pickFileFor('decrypt')
        d, n  = int(privateKey['d']), int(privateKey['n'])

        with Bar('Processing', max=len(srcFile.read())/KEY_LENGTH_IN_BYTES) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(KEY_LENGTH_IN_BYTES)
                if not char: break
                decryptedChar = pow(int.from_bytes(char, byteorder='big'), d, n)
                decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
                dstFile.write(decryptedByte)
                bar.next()
        srcFile.close(); dstFile.close()