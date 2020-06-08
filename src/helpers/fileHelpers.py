from .pickFile import pickFile
from .colors import typedText
from os.path import splitext, isfile
from .constants import ASSYMETRIC_ALGORITHMS



def writeParams(key, alg):
    root = 'keys/'; filename = typedText('Enter filename with key: ')

    pkFile = open(root + alg.lower() + '.' + filename +'.pk', 'wb')
    for param in key['private']: pkFile.write(param.encode() + ': '.encode() + str(hex(key['private'][param])[2:].upper()).encode() + '\n'.encode())
    pkFile.close()
    
    if alg in ASSYMETRIC_ALGORITHMS:
        pubkFile = open(root + alg.lower() + '.' + filename +'.pubk', 'wb')
        for param in key['public']: pubkFile.write(param.encode() + ': '.encode() + str(hex(key['public'][param])[2:].upper()).encode() + '\n'.encode())
        pubkFile.close()


def readParams():
    pathToParams = pickFile()

    keys = {}
    fileParams = open(pathToParams, 'r').readlines()
    for line in fileParams:
        trim = line.find(':')
        key = line[:trim]
        keys[key] = int(line[trim+2:], 16)
    return keys



def pickFileFor(purpose):
    srcFilePath = pickFile()
    filename, file_extension = splitext(srcFilePath)
    if purpose == 'encrypt': dstFilePath = filename + '.encrypted' + file_extension
    elif purpose == 'decrypt': 
        if filename[-9:] == 'encrypted': dstFilePath = filename[:-9] + 'decrypted' + file_extension
        else: raise Exception('You are trying to decrypt an unencrypted file.')
    
    elif purpose == 'sign': dstFilePath = filename + '.sign'
    elif purpose == 'validate':
        if not isfile(filename + '.sign'): raise Exception('Signature not exist')
        if file_extension == '.sign': raise Exception('You picked signature. Nonsense.')
        return open(srcFilePath, 'rb'), open(filename + '.sign', 'rb')

    srcFile = open(srcFilePath, 'rb')
    dstFile = open(dstFilePath, 'wb')
    return srcFile, dstFile