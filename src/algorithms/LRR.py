from ..helpers.fileHelpers import pickFileFor
from ..helpers.constants import KEY_LENGTH_IN_BITS, KEY_LENGTH_IN_BYTES


class LRR:

    TAPS = (8,7,6,1)

    generateKey = staticmethod(lambda: {'private': {'seed': int.from_bytes(getattr(__import__('os'), 'urandom')(KEY_LENGTH_IN_BYTES), byteorder='big')}})
    

    @staticmethod
    def generateGamma(shift_register_state):
        xor_input = 1; nbits = shift_register_state.bit_length()
        for tap in LRR.TAPS:
            if (shift_register_state & (1<<(tap-1))) != 0:
                xor_input ^= 1
        shift_register_state = (xor_input << nbits-1) + (shift_register_state >> 1)
        return shift_register_state


    @staticmethod
    def encrypt(key):
        from progress.bar import Bar

        srcFile, dstFile = pickFileFor('encrypt')
        shift_register_state = key['seed']

        with Bar('Processing', max=len(srcFile.read())) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(1)
                if not char: break
                gamma = LRR.generateGamma(shift_register_state)
                shift_register_state = gamma
                cipherChar = gamma ^ int.from_bytes(char, byteorder='big')
                cipherBytes = cipherChar.to_bytes(KEY_LENGTH_IN_BYTES, byteorder='big')
                # print(cipherBytes); exit()
                dstFile.write(cipherBytes)
                bar.next()
        srcFile.close(); dstFile.close()


    @staticmethod
    def decrypt(key):
        from progress.bar import Bar

        srcFile, dstFile = pickFileFor('decrypt')
        shift_register_state = key['seed']

        with Bar('Processing', max=len(srcFile.read())/(KEY_LENGTH_IN_BYTES)) as bar:
            srcFile.seek(0)
            while True:
                char = srcFile.read(KEY_LENGTH_IN_BYTES)
                if not char: break
                gamma = LRR.generateGamma(shift_register_state)
                shift_register_state = gamma
                decryptedChar = gamma ^ int.from_bytes(char, byteorder='big')
                decryptedByte = decryptedChar.to_bytes(1, byteorder='big')
                dstFile.write(decryptedByte)
                bar.next()
        srcFile.close(); dstFile.close()