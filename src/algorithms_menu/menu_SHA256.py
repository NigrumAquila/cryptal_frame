from ..helpers.constants import SHA256_choice, BACK, EXIT
from ..helpers.colors import printTextAndValue, printText, end, warning
from ..helpers.fileHelpers import writeParams
from ..helpers.pickFile import pickFile
from ..algorithms.SHA256 import SHA256
from ..helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(SHA256_choice) + '; b - BACK TO ALGORITHMS SELECTION; e - EXIT: ').lower()

    if case == SHA256_choice['GENERATE_DIGEST']:
        filename = pickFile()
        digest = SHA256.digest(open(filename, 'rb').read()).hex()
        params = {'filename': filename, 'digest': digest}
        printTextAndValue('digest', digest)
        writeParams(params, 'SHA256')
        printText('Digest generated.')

    elif case == BACK:
        break

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Wrong selection. Please, try again.')