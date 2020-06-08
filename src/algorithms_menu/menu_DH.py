from ..helpers.constants import DH_choice, BACK, EXIT
from ..helpers.colors import printText, printTextAndValue, end, warning
from ..helpers.fileHelpers import writeParams
from ..algorithms.DH import DH
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(DH_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == DH_choice['GENERATE_SECRET']:
        secret = DH.generateSharedSecret()
        writeParams(secret, 'DH')
        printTextAndValue('secret', secret)
        printText('Secret generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')