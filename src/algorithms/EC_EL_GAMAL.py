from .EC import EC
from ..helpers.fileHelpers import pickFileFor, readParams
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
        point = readParams()
        k = randint(0, publicKey['order'])
        a, b = EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k), EC.addition({'x': point['x'],'y': point['y']}, EC.multiply({'x': publicKey['x'], 'y': publicKey['y']}, k))
        
        return {a, b}
        

    @staticmethod
    def decrypt(privateKey):
        pass