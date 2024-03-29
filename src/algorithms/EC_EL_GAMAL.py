from src.algorithms.EC import EC
from core.helpers.fileHelpers import pickFileFor, readParams
from random import randint


class EC_EL_GAMAL():

    generateKeys = staticmethod(lambda: EC.generateKeys())


    @staticmethod
    def generatePoint():
        params = readParams()
        point = EC.multiply({'x': params['x'], 'y': params['y']}, randint(1, params['order'] - 1))
        return {'x': point['x'], 'y': point['y']}

    @staticmethod
    def encrypt(publicKey):
        srcFile, dstFile = pickFileFor('encrypt')
        point = readParams(srcFile.name)
        k = randint(0, publicKey['order'])
        a = EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k)
        b = EC.addition({'x': point['x'],'y': point['y']}, EC.multiply({'x': publicKey['Qx'], 'y': publicKey['Qy']}, k))
        for param in a.keys(): dstFile.write('a'.encode() + param.encode() + ': '.encode() + str(hex(a[param])[2:]).encode() + '\n'.encode())
        for param in b.keys(): dstFile.write('b'.encode() + param.encode() + ': '.encode() + str(hex(b[param])[2:]).encode() + '\n'.encode())
        srcFile.close; dstFile.close()
        

    @staticmethod
    def decrypt(privateKey):
        srcFile, dstFile = pickFileFor('decrypt')
        cipher = readParams(srcFile.name)
        decryptedPoint = EC.addition({'x': cipher['bx'], 'y': cipher['by']}, EC.reflectPoint(EC.multiply({'x': cipher['ax'],'y': cipher['ay']}, privateKey['d'])))
        for param in decryptedPoint.keys(): dstFile.write(param.encode() + ': '.encode() + str(hex(decryptedPoint[param])[2:]).encode() + '\n'.encode())
        srcFile.close(); dstFile.close()
