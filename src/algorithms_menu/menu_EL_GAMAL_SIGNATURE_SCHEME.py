from src.algorithms.EL_GAMAL_SIGNATURE_SCHEME import EL_GAMAL_SIGNATURE_SCHEME
from src.constants.algorithmMenuConstants import EL_GAMAL_SIGNATURE_SCHEME_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printTextAndValue, printText, end, warning
from core.helpers.fileHelpers import writeParams, readParams
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(EL_GAMAL_SIGNATURE_SCHEME_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == EL_GAMAL_SIGNATURE_SCHEME_choice['GENERATE_KEYS']:
        keys = EL_GAMAL_SIGNATURE_SCHEME.generateKeys()
        printTextAndValue('public key', keys['public'])
        printTextAndValue('private key', keys['private'])
        writeParams(keys, 'EL_GAMAL_SIGNATURE_SCHEME')
        printText('Keys generated.')

    elif case == EL_GAMAL_SIGNATURE_SCHEME_choice['SELECT_PUBLIC_KEY']:
        pubKey = readParams()
        printText('Public key selected. You can verify.')

    elif case == EL_GAMAL_SIGNATURE_SCHEME_choice['SELECT_PRIVATE_KEY']:
        privKey = readParams()
        printText('Private key selected. You can sign.')
    
    elif case == EL_GAMAL_SIGNATURE_SCHEME_choice['SIGN_FILE']:
        if not 'privKey' in locals(): printText('Key is not defined.'); continue
        if privKey == '': printText('Key is empty.'); continue

        EL_GAMAL_SIGNATURE_SCHEME.sign(privKey)
        printText('File signed.')

    elif case == EL_GAMAL_SIGNATURE_SCHEME_choice['VERIFY_FILE']:
        if not 'pubKey' in locals(): printText('Key is not defined.'); continue
        if pubKey == '': printText('Key is empty.'); continue

        verdict = 'successful' if EL_GAMAL_SIGNATURE_SCHEME.verify(pubKey) else 'failed'
        printText('Verification  '+ verdict + '.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')