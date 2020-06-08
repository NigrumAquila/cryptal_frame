from ..helpers.constants import RSA_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.RSA import RSA


while True:
    case = input('Select action: 1 - Generate keys; 2 - Select public key; 3 - Select private key; 4 - Encrypt file; 5 - Decrypt file; b - Back to algorithms selection; e - Exit: ')

    if case == RSA_choice['GENERATE_KEYS']:
        keys = RSA.generateKeys()
        printTextAndValue('public key', keys['public'])
        printTextAndValue('private key', keys['private'])
        writeParams(keys, 'RSA')
        printText('Keys generated.')

    elif case == RSA_choice['SELECT_PUBLIC_KEY']:
        pubKey = readParams()
        printText('Public key selected. You can encrypt.')

    elif case == RSA_choice['SELECT_PRIVATE_KEY']:
        privKey = readParams()
        printText('Private key selected. You can decrypt.')

    elif case == RSA_choice['ENCRYPT_FILE']:
        if not 'pubKey' in locals(): print('Key is not defined.'); continue
        if pubKey == '': print('Key is empty.'); continue

        RSA.encrypt(pubKey)
        printText('File encrypted.')

    elif case == RSA_choice['DECRYPT_FILE']:
        if not 'privKey' in locals(): print('Key is not defined.'); continue
        if privKey == '': print('Key is empty.'); continue

        RSA.decrypt(privKey)
        printText('File decrypted.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')