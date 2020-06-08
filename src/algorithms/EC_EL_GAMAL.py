from .EC import EC
from ..helpers.fileHelpers import pickFileFor
from random import randint


class EC_EL_GAMAL():

    generateKeys = staticmethod(lambda: EC.generateKeys())


    @staticmethod
    def generatePoint():
        pass


    @staticmethod
    def encrypt(publicKey):
        pass
        

    @staticmethod
    def decrypt(privateKey):
        pass