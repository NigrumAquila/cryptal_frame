from src.algorithms.AES import AES
from src.constants.algorithmMenuConstants import AES_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printTextAndValue, printText, end, warning
from core.helpers.fileHelpers import writeParams, readParams
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(AES_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == AES_choice['GENERATE_KEY']:
        key = AES.generateKey()
        printTextAndValue('key', key)
        writeParams(key, 'AES')
        printText('Key generated.')

    elif case == AES_choice['SELECT_KEY']:
        key = AES.hashKey(readParams()['secret'])
        printText('Key selected.')
    
    elif case == AES_choice['ENCRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        AES.encrypt(key)
        printText('File encrypted.')

    elif case == AES_choice['DECRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        AES.decrypt(key)
        printText('File decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')