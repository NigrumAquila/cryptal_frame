from ..helpers.constants import EC_EL_GAMAL_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.EC_EL_GAMAL import EC_EL_GAMAL
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(EC_EL_GAMAL_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == EC_EL_GAMAL_choice['GENERATE_KEYS']:
        keys = EC_EL_GAMAL.generateKeys()
        printTextAndValue('public key', keys['public'])
        printTextAndValue('private key', keys['private'])
        writeParams(keys, 'EC_EL_GAMAL')
        printText('Keys generated.')

    elif case == EC_EL_GAMAL_choice['GENERATE_POINT']:
        pass

    elif case == EC_EL_GAMAL_choice['SELECT_PUBLIC_KEY']:
        pubKey = readParams()
        printText('Public key selected. You can validate.')

    elif case == EC_EL_GAMAL_choice['SELECT_PRIVATE_KEY']:
        privKey = readParams()
        printText('Private key selected. You can sign.')
    
    elif case == EC_EL_GAMAL_choice['ENCRYPT_POINT']:
        if not 'privKey' in locals(): printText('Key is not defined.'); continue
        if privKey == '': printText('Key is empty.'); continue

        printText('Point encrypted.')

    elif case == EC_EL_GAMAL_choice['DECRYPT_POINT']:
        if not 'pubKey' in locals(): printText('Key is not defined.'); continue
        if pubKey == '': printText('Key is empty.'); continue

        printText('Point decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')