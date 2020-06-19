from src.algorithms.SHA256 import SHA256
from src.constants.algorithmMenuConstants import SHA256_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printTextAndValue, printText, end, warning
from core.helpers.fileHelpers import writeParams, pickFileFor
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(SHA256_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == SHA256_choice['GENERATE_DIGEST']:
        fileStream, filepath = pickFileFor('digest')
        digest = SHA256.digest(fileStream.read()).hex()
        params = {'filepath': filepath, 'digest': digest}
        printTextAndValue('digest', digest)
        writeParams(params, 'SHA256')
        printText('Digest generated.')
        fileStream.close()

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')