from ..helpers.constants import ECDH_choice, BACK, EXIT
from ..helpers.colors import printText, printTextAndValue, end, warning
from ..helpers.fileHelpers import writeParams
from ..algorithms.ECDH import ECDH
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ECDH_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == ECDH_choice['GENERATE_SECRET']:
        secret = ECDH.generateSharedSecret()
        writeParams(secret, 'ECDH')
        printTextAndValue('secret', secret)
        printText('Secret generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')