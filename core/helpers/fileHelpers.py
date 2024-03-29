from os.path import splitext, isfile
from core.styles.colors import typedText
from src.constants.algorithmConstants import ASSYMETRIC_ALGORITHMS, ENCRYPTION_ALGORITHMS, HASH_FUNCTIONS



def writeParams(params, alg):
    if alg == 'EC_EL_GAMAL_WRITE_POINT':
        root = 'points/'; filename = typedText('Enter filename with point: ')
        pointFile = open(root + 'ec_point.' + filename + '.p', 'wb')
        for param in params.keys(): pointFile.write(param.encode() + ': '.encode() + str(hex(params[param])[2:]).encode() + '\n'.encode())
        pointFile.close(); return

    if alg in HASH_FUNCTIONS:
        digestFile = open(params['filepath'] + '.' + alg.lower() + '_digest', 'wb')
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
    if pathToParams == None: pathToParams = __pickFile()
    if pathToParams == '': raise Exception('File not selected.')

    params = {}
    fileParams = open(pathToParams, 'r').readlines()
    for line in fileParams:
        trim = line.find(':')
        param = line[:trim]
        params[param] = int(line[trim+2:], 16)
    return params



def pickFileFor(purpose):
    srcFilePath = __pickFile()
    if srcFilePath == '': raise Exception('File not selected.')
    filename, file_extension = splitext(srcFilePath)

    if purpose == 'encrypt': dstFilePath = filename + '.encrypted' + file_extension
    elif purpose == 'decrypt': 
        if filename[-9:] == 'encrypted': dstFilePath = filename[:-9] + 'decrypted' + file_extension
        else: raise Exception('You are trying to decrypt an unencrypted file.')
    
    elif purpose == 'sign': dstFilePath = srcFilePath + '.sign'
    elif purpose == 'verify':
        if not isfile(srcFilePath + '.sign'): raise Exception('Signature not exist')
        if file_extension == '.sign': raise Exception('You picked signature. Nonsense.')
        return open(srcFilePath, 'rb'), open(srcFilePath + '.sign', 'rb')

    elif purpose == 'digest': return open(srcFilePath, 'rb'), srcFilePath

    elif purpose == 'get_path': return srcFilePath

    srcFile = open(srcFilePath, 'rb')
    dstFile = open(dstFilePath, 'wb')
    return srcFile, dstFile



def truncateFile(filepath):
    with open(filepath, 'rb+') as srcFile:
        srcFile.seek(0, 2); srcFile.seek(srcFile.tell() - 16, 0)
        data = srcFile.read()
        if chr(0).encode() in data: truncateSize = data.count('\x00'.encode())
        srcFile.seek(0, 2); srcFile.seek(srcFile.tell() - truncateSize, 0)
        srcFile.truncate()




def __pickFile(title='Open'):
    from tkinter import filedialog, Tk

    if not 'root' in locals(): 
        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()

    return filedialog.askopenfilename(title=title)