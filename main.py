import src.helpers.encoding
from src.helpers.colors import changeColor, defaultColor, warning, printText, printValue, printTextAndValue, typedText, end
from src.helpers.fileHelpers import readParams, writeParams
from src.helpers.constants import ALGORITHM_choice, RSA_choice, LRR_choice, ECDSA_choice, EL_GAMAL_choice, BACK, EXIT, ALGORITHM_MENU_MODULE_SPACE
from src.helpers.deleteModuleIfReturn import deleteModuleIfReturn
from src.helpers.dictionaryKeyParser import dictionaryKeyParser


while True:
    case = input('Select action: 1 - RSA; 2 - Linear recurrent register; 3 - ECDSA; 4 - El Gamal; e - to exit: ')
    if case == ALGORITHM_choice['RSA']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn()

    elif case == ALGORITHM_choice['LRR']:
        from src.algorithms.LRR import LRR

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
                if not 'key' in locals(): print('Key is not defined.'); continue
                if key == '': print('Key is empty.'); continue

                LRR.encrypt(key)
                printText('File encrypted.')

            elif case == LRR_choice['DECRYPT_FILE']:
                if not 'key' in locals(): print('Key is not defined.'); continue
                if key == '': print('Key is empty.'); continue

                LRR.decrypt(key)
                printText('File decrypted.')

            elif case == BACK:
                break

            elif case == EXIT:
                end('Execution completed.')

            else:
                warning('Wrong selection. Please, try again.')

    elif case == ALGORITHM_choice['ECDSA']:
        from src.algorithms.ECDSA import ECDSA

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
                if not 'privKey' in locals(): print('Key is not defined.'); continue
                if privKey == '': print('Key is empty.'); continue

                ECDSA.sign(privKey)
                printText('File signed.')

            elif case == ECDSA_choice['VALIDATE_FILE']:
                if not 'pubKey' in locals(): print('Key is not defined.'); continue
                if pubKey == '': print('Key is empty.'); continue

                verdict = 'successfully' if ECDSA.validate(pubKey) else 'failed'
                printText('Validation '+ verdict + '.')

            elif case == BACK:
                break

            elif case == EXIT:
                end('Execution completed.')

            else:
                warning('Wrong selection. Please, try again.')

    if case == ALGORITHM_choice['EL_GAMAL']:
        from src.algorithms.El_Gamal import El_Gamal

        while True:
            case = input('Select action: 1 - Generate keys; 2 - Select public key; 3 - Select private key; 4 - Encrypt file; 5 - Decrypt file; b - Back to algorithms selection; e - Exit: ')

            if case == EL_GAMAL_choice['GENERATE_KEYS']:
                keys = El_Gamal.generateKeys()
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
                if not 'pubKey' in locals(): print('Key is not defined.'); continue
                if pubKey == '': print('Key is empty.'); continue

                El_Gamal.encrypt(pubKey)
                printText('File encrypted.')

            elif case == EL_GAMAL_choice['DECRYPT_FILE']:
                if not 'privKey' in locals(): print('Key is not defined.'); continue
                if privKey == '': print('Key is empty.'); continue

                El_Gamal.decrypt(privKey)
                printText('File decrypted.')

            elif case == BACK:
                break

            elif case == EXIT:
                end('Execution completed.')

            else:
                warning('Wrong selection. Please, try again.')

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Select algorithm.')
