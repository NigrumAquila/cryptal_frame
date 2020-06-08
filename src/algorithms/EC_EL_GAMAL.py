from .EC import EC
from ..helpers.fileHelpers import pickFileFor, readParams, writeParams
from random import randint
from ..helpers.pickFile import pickFile


class EC_EL_GAMAL():

    generateKeys = staticmethod(lambda: EC.generateKeys())


    @staticmethod
    def generatePoint():
        params = readParams()
        point = EC.multiply({'x': params['x'], 'y': params['y']}, randint(1, params['order'] - 1))
        return {'x': point['x'], 'y': point['y']}

    @staticmethod
    def encrypt(publicKey):
        filename = pickFile()
        point = readParams(filename)
        k = randint(0, publicKey['order'])
        a = EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k)
        b = EC.addition({'x': point['x'],'y': point['y']}, EC.multiply({'x': publicKey['Qx'], 'y': publicKey['Qy']}, k))
        dstFile = open(filename[:-2] + '.encrypted' + filename[-2:], 'wb')
        
        # cipher = [a, b]
        # for half in cipher:
        #     for param in half.keys(): dstFile.write(param.encode() + ': '.encode() + str(half[param]).encode() + '\n'.encode())
        
        for param in a.keys(): dstFile.write('a'.encode() + param.encode() + ': '.encode() + str(hex(a[param])[2:]).encode() + '\n'.encode())
        for param in b.keys(): dstFile.write('b'.encode() + param.encode() + ': '.encode() + str(hex(b[param])[2:]).encode() + '\n'.encode())
        dstFile.close()
        

    @staticmethod
    def decrypt(privateKey):
        filename = pickFile()
        cipher = readParams(filename)
        decryptedPoint = EC.addition({'x': cipher['bx'], 'y': cipher['by']}, EC.reflectPoint(EC.multiply({'x': cipher['ax'],'y': cipher['ay']}, privateKey['d'])))
        dstFile = open(filename[:-12] + '.decrypted' + filename[-2:], 'wb')
        for param in decryptedPoint.keys(): dstFile.write(param.encode() + ': '.encode() + str(hex(decryptedPoint[param])[2:]).encode() + '\n'.encode())
        dstFile.close()
