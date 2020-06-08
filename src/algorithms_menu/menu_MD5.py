from ..helpers.constants import MD5_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams
from ..helpers.pickFile import pickFile
from ..algorithms.MD5 import MD5
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(MD5_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == MD5_choice['GENERATE_DIGEST']:
        filename = pickFile()
        digest = MD5(open(filename, 'rb').read()).hexdigest()
        params = {'filename': filename, 'digest': digest}
        printTextAndValue('digest', digest)
        writeParams(params, 'MD5')
        printText('Digest generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')