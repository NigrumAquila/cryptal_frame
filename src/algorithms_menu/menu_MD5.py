from src.algorithms.MD5 import MD5
from src.constants.algorithmMenuConstants import MD5_choice
from core.constants.interfaceConstants import BACK, EXIT
from core.styles.colors import printTextAndValue, printText, end, warning
from core.helpers.fileHelpers import writeParams, pickFileFor
from core.helpers.dictionaryHelpers import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(MD5_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == MD5_choice['GENERATE_DIGEST']:
        fileStream, filepath = pickFileFor('digest')
        digest = MD5(fileStream.read()).hexdigest()
        params = {'filepath': filepath, 'digest': digest}
        printTextAndValue('digest', digest)
        writeParams(params, 'MD5')
        printText('Digest generated.')
        fileStream.close()

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')