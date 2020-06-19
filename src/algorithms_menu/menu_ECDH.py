from src.algorithms.ECDH import ECDH
from src.constants.algorithmMenuConstants import ECDH_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printText, printTextAndValue, end, warning
from core.helpers.fileHelpers import writeParams
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ECDH_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == ECDH_choice['GENERATE_SECRET']:
        secret = ECDH.generateSharedSecret()
        printTextAndValue('secret', secret)
        writeParams(secret, 'ECDH')
        printText('Secret generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')