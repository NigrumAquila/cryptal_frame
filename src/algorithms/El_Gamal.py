from core.math.findPrimitiveRoot import findPrimitiveRoot
from core.math.multiplicativeInverse import multiplicativeInverse
from core.helpers.fileHelpers import pickFileFor
from src.constants.keyConstants import KEY_LENGTH_IN_BITS, KEY_LENGTH_IN_BYTES
from sympy import randprime
from random import randint


class EL_GAMAL():

    @staticmethod
    def generateKeys():
        p = randprime(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS)
        g = findPrimitiveRoot(p)
        g = pow(g, 2, p)
        x = randint(1, (p-1) // 2)
        y = pow(g, x, p)
        return {'public': {'y': y, 'p': p, 'g': g}, 'private': {'x': x, 'p': p}}


    @staticmethod
    def encrypt(publicKey):
        from tqdm import tqdm as Bar

        srcFile, dstFile = pickFileFor('encrypt')
        k = randint(1, publicKey['p'] - 1)
        a = pow(publicKey['g'], k, publicKey['p'])
        dstFile.write(a.to_bytes(KEY_LENGTH_IN_BYTES, byteorder='big'))

        with Bar(total=len(srcFile.read())) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(1)
                if not char: break
                cipherChar = (pow(publicKey['y'], k, publicKey['p']) * int.from_bytes(char, byteorder='big')) % publicKey['p']
                cipherBytes = cipherChar.to_bytes(KEY_LENGTH_IN_BYTES, byteorder='big')
                dstFile.write(cipherBytes)
                bar.update()
        srcFile.close(); dstFile.close()


    @staticmethod
    def decrypt(privateKey):
        from tqdm import tqdm as Bar

        srcFile, dstFile = pickFileFor('decrypt')
        a = int.from_bytes(srcFile.read(KEY_LENGTH_IN_BYTES), byteorder='big')

        with Bar(total=len(srcFile.read())/(KEY_LENGTH_IN_BYTES)) as bar:
            srcFile.seek(KEY_LENGTH_IN_BYTES)
            while True:
                char = srcFile.read(KEY_LENGTH_IN_BYTES)
                if not char: break
                s = pow(a, privateKey['x'], privateKey['p'])
                decryptedChar = (int.from_bytes(char, byteorder='big') * pow(s, privateKey['p']-2, privateKey['p'])) % privateKey['p']
                decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
                dstFile.write(decryptedByte)
                bar.update()
        srcFile.close(); dstFile.close()