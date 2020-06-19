from src.algorithms.EC import EC
from src.algorithms.MD5 import MD5
from core.helpers.fileHelpers import pickFileFor
from core.math.multiplicativeInverse import multiplicativeInverse
from random import randint



class ECDSA():

    generateKeys = staticmethod(lambda: EC.generateKeys())

    def sign(privateKey):
        srcFile, dstFile = pickFileFor('sign')
        hashValue = int.from_bytes(MD5(srcFile.read()).digest(), byteorder='big')
        randomNumber = randint(1, privateKey['order'] - 1)
        point = EC.multiply({'x': privateKey['x'], 'y': privateKey['y']}, randomNumber)
        signature = {'r': point['x'], 's': multiplicativeInverse(randomNumber, privateKey['order']) * (hashValue + point['x'] * privateKey['d']) % privateKey['order']}
        for param in signature:
            dstFile.write(param.encode() + ': '.encode() + str(hex(signature[param])[2:].upper()).encode() + '\n'.encode())
        srcFile.close(); dstFile.close()


    def verify(publicKey):
        assert EC.validatePoint({'x': publicKey['Qx'], 'y': publicKey['Qy']})
        assert EC.multiply({'x': publicKey['Qx'], 'y': publicKey['Qy']}, publicKey['order']) == EC.ZERO_POINT

        srcFile, signFile = pickFileFor('verify')
        hashValue = int.from_bytes(MD5(srcFile.read()).digest(), byteorder='big')
        signature = {}
        for line in signFile.readlines():
            trim = line.decode().find(':') 
            key = line.decode()[:trim]
            signature[key] = int(line.decode()[trim+2:], 16)
        w = multiplicativeInverse(signature['s'], publicKey['order'])
        u1, u2 = hashValue * w % publicKey['order'], signature['r'] * w % publicKey['order']
        point = EC.addition(EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, u1), EC.multiply({'x': publicKey['Qx'], 'y': publicKey['Qy']}, u2))
        srcFile.close(); signFile.close()
        return point['x'] % publicKey['order'] == signature['r']