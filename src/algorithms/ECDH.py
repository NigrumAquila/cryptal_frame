from src.algorithms.EC import EC
from core.helpers.fileHelpers import readParams, pickFileFor
from src.constants.keyConstants import KEY_LENGTH_IN_BITS
from random import randint


class ECDH():

    @staticmethod
    def generateSharedSecret():
        params = readParams()
        
        privateKeyAlice = params.copy(); privateKeyAlice['d'] = randint(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS)
        privateKeyBob = params.copy(); privateKeyBob['d'] = randint(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS)
        Q_Alice = EC.multiply({'x': params['x'], 'y': params['y']}, privateKeyAlice['d'])
        Q_Bob = EC.multiply({'x': params['x'], 'y': params['y']}, privateKeyBob['d'])
        publicKeyAlice = params.copy(); publicKeyAlice['Qx'] = Q_Alice['x']; publicKeyAlice['Qy'] = Q_Alice['y']
        publicKeyBob = params.copy(); publicKeyBob['Qx'] = Q_Bob['x']; publicKeyBob['Qy'] = Q_Bob['y']
        sharedSecredAlice = EC.multiply({'x': publicKeyBob['Qx'], 'y': publicKeyBob['Qy']}, privateKeyAlice['d'])
        sharedSecredBob = EC.multiply({'x': publicKeyAlice['Qx'], 'y': publicKeyAlice['Qy']}, privateKeyBob['d'])

        assert EC.validatePoint({'x': publicKeyAlice['Qx'], 'y': publicKeyAlice['Qy']}) and EC.validatePoint({'x': publicKeyBob['Qx'], 'y': publicKeyBob['Qy']})
        assert EC.multiply({'x': publicKeyAlice['Qx'], 'y': publicKeyAlice['Qy']}, publicKeyAlice['order']) == EC.ZERO_POINT
        assert EC.multiply({'x': publicKeyBob['Qx'], 'y': publicKeyBob['Qy']}, publicKeyBob['order']) == EC.ZERO_POINT
        assert sharedSecredAlice == sharedSecredBob

        return {'private': {'secret': sharedSecredAlice['x']}}