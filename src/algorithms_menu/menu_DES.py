from ..helpers.constants import DES_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.DES import DES
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(DES_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()
    
    if case == DES_choice['GENERATE_KEY']:
        key = DES.generateKey()
        printTextAndValue('key', key)
        writeParams(key, 'DES')
        printText('Key generated.')

    elif case == DES_choice['SELECT_KEY']:
        key = readParams()['secret'].to_bytes(16, byteorder='big')[:8]
        printText('Key selected.')
    
    elif case == DES_choice['ENCRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        DES.encrypt(key)
        printText('File encrypted.')

    elif case == DES_choice['DECRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        DES.decrypt(key)
        printText('File decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')