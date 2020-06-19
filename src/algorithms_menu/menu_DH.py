from src.algorithms.DH import DH
from src.constants.algorithmMenuConstants import DH_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printText, printTextAndValue, end, warning
from core.helpers.fileHelpers import writeParams
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(DH_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == DH_choice['GENERATE_SECRET']:
        secret = DH.generateSharedSecret()
        printTextAndValue('secret', secret)
        writeParams(secret, 'DH')
        printText('Secret generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')