from .pickFile import pickFile
from .colors import typedText
from os.path import splitext, isfile
from .constants import ASSYMETRIC_ALGORITHMS, ENCRYPTION_ALGORITHMS



def writeParams(params, alg):
    if alg == 'EC_EL_GAMAL_WRITE_POINT':
        root = 'points/'; filename = typedText('Enter filename with point: ')
        pointFile = open(root + 'ec_point.' + filename + '.p', 'wb')
        for param in params.keys(): pointFile.write(param.encode() + ': '.encode() + str(params[param]).encode() + '\n'.encode())
        pointFile.close(); return

    if alg == 'MD5':
        digestFile = open(params['filename'] + '.' + alg.lower() + '_digest', 'wb')
        digestFile.write(params['digest'].upper().encode())
        digestFile.close(); return

    if alg in ENCRYPTION_ALGORITHMS:
        root = 'keys/'; filename = typedText('Enter filename with key: ')

        pkFile = open(root + alg.lower() + '.' + filename +'.pk', 'wb')
        for param in params['private']: pkFile.write(param.encode() + ': '.encode() + str(hex(params['private'][param])[2:].upper()).encode() + '\n'.encode())
        pkFile.close()
        
        if alg in ASSYMETRIC_ALGORITHMS and alg not in ['DH', 'ECDH']:
            pubkFile = open(root + alg.lower() + '.' + filename +'.pubk', 'wb')
            for param in params['public']: pubkFile.write(param.encode() + ': '.encode() + str(hex(params['public'][param])[2:].upper()).encode() + '\n'.encode())
            pubkFile.close()


def readParams(pathToParams=None):
    if pathToParams == None: pathToParams = pickFile()

    params = {}
    fileParams = open(pathToParams, 'r').readlines()
    for line in fileParams:
        trim = line.find(':')
        param = line[:trim]
        params[param] = int(line[trim+2:], 16)
    return params



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