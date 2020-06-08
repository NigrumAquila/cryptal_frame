from ..helpers.constants import ECDSA_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams, readParams
from ..algorithms.ECDSA import ECDSA

while True:
    case = input('Select action: 1 - Generate keys; 2 - Select public key; 3 - Select private key; 4 - Sign file; 5 - Validate file; e - Exit: ')

    if case == ECDSA_choice['GENERATE_KEYS']:
        keys = ECDSA.generateKeys()
        printTextAndValue('public key', keys['public'])
        printTextAndValue('private key', keys['private'])
        writeParams(keys, 'EC')
        printText('Keys generated.')

    elif case == ECDSA_choice['SELECT_PUBLIC_KEY']:
        pubKey = readParams()
        printText('Public key selected. You can validate.')

    elif case == ECDSA_choice['SELECT_PRIVATE_KEY']:
        privKey = readParams()
        printText('Private key selected. You can sign.')
    
    elif case == ECDSA_choice['SIGN_FILE']:
        if not 'privKey' in locals(): printText('Key is not defined.'); continue
        if privKey == '': printText('Key is empty.'); continue

        ECDSA.sign(privKey)
        printText('File signed.')

    elif case == ECDSA_choice['VALIDATE_FILE']:
        if not 'pubKey' in locals(): printText('Key is not defined.'); continue
        if pubKey == '': printText('Key is empty.'); continue

        verdict = 'successfully' if ECDSA.validate(pubKey) else 'failed'
        printText('Validation '+ verdict + '.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')