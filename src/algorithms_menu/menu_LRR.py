from ..helpers.constants import LRR_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.LRR import LRR

while True:
    case = input('Select action: 1 - Generate key; 2 - Select key; 3 - Encrypt file; 4 - Decrypt file; b - Back to algorithms selection; e - Exit: ')

    if case == LRR_choice['GENERATE_KEY']:
        key = LRR.generateKey()
        printTextAndValue('key', key)
        writeParams(key, 'LRR')
        printText('Key generated.')

    elif case == LRR_choice['SELECT_KEY']:
        key = readParams()
        printText('Key selected.')
    
    elif case == LRR_choice['ENCRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        LRR.encrypt(key)
        printText('File encrypted.')

    elif case == LRR_choice['DECRYPT_FILE']:
        if not 'key' in locals(): printText('Key is not defined.'); continue
        if key == '': printText('Key is empty.'); continue

        LRR.decrypt(key)
        printText('File decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')