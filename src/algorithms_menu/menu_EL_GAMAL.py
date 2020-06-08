from ..helpers.constants import EL_GAMAL_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.EL_GAMAL import EL_GAMAL
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(EL_GAMAL_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == EL_GAMAL_choice['GENERATE_KEYS']:
        keys = EL_GAMAL.generateKeys()
        printTextAndValue('public key', keys['public'])
        printTextAndValue('private key', keys['private'])
        writeParams(keys, 'EL_GAMAL')
        printText('Keys generated.')

    elif case == EL_GAMAL_choice['SELECT_PUBLIC_KEY']:
        pubKey = readParams()
        printText('Public key selected. You can encrypt.')

    elif case == EL_GAMAL_choice['SELECT_PRIVATE_KEY']:
        privKey = readParams()
        printText('Private key selected. You can decrypt.')

    elif case == EL_GAMAL_choice['ENCRYPT_FILE']:
        if not 'pubKey' in locals(): printText('Key is not defined.'); continue
        if pubKey == '': printText('Key is empty.'); continue

        EL_GAMAL.encrypt(pubKey)
        printText('File encrypted.')

    elif case == EL_GAMAL_choice['DECRYPT_FILE']:
        if not 'privKey' in locals(): printText('Key is not defined.'); continue
        if privKey == '': printText('Key is empty.'); continue

        EL_GAMAL.decrypt(privKey)
        printText('File decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')