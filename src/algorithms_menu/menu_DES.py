from src.algorithms.DES import DES
from src.constants.algorithmMenuConstants import DES_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printTextAndValue, printText, end, warning
from core.helpers.fileHelpers import writeParams, readParams
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


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