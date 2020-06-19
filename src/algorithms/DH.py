from core.math.findPrimitiveRoot import findPrimitiveRoot
from src.constants.keyConstants import KEY_LENGTH_IN_BITS
from random import randint
from sympy import randprime


class DH():

    @staticmethod
    def generateSharedSecret():
        prime = randprime(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS)
        generator = findPrimitiveRoot(prime)
        
        keys = {
            'private_key_Alice': randint(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS),
            'private_key_Bob': randint(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS),
        }

        keys['public_key_Alice'] = pow(generator, keys['private_key_Alice'], prime)
        keys['public_key_Bob'] = pow(generator, keys['private_key_Bob'], prime)
        keys['shared_secret_Alice'] = pow(keys['public_key_Bob'], keys['private_key_Alice'], prime)
        keys['shared_secret_Bob'] = pow(keys['public_key_Alice'], keys['private_key_Bob'], prime)
        return {'private': {'secret': keys['shared_secret_Alice']}}