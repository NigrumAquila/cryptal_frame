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
        a, b = EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k), EC.addition({'x': point['x'],'y': point['y']}, EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k))
        cipher = [a, b]
        dstFile = open(filename[:-2] + '.encrypted' + filename[-2:], 'wb')
        
        # for half in cipher:
        #     for param in half.keys(): dstFile.write(param.encode() + ': '.encode() + str(half[param]).encode() + '\n'.encode())
            
        for param in a.keys(): dstFile.write('a'.encode() + param.encode() + ': '.encode() + str(a[param]).encode() + '\n'.encode())
        for param in b.keys(): dstFile.write('b'.encode() + param.encode() + ': '.encode() + str(b[param]).encode() + '\n'.encode())
        dstFile.close()
        

    @staticmethod
    def decrypt(privateKey):
        pass