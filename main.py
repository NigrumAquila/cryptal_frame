import src.helpers.encoding
from src.helpers.colors import changeColor, defaultColor, warning, printText, printValue, printTextAndValue, typedText, end
from src.helpers.fileHelpers import readParams, writeParams
from src.helpers.constants import ALGORITHM_choice, RSA_choice, LRR_choice, ECDSA_choice, EL_GAMAL_choice, BACK, EXIT, ALGORITHM_MENU_MODULE_SPACE
from src.helpers.deleteModuleIfReturn import deleteModuleIfReturn
from src.helpers.dictionaryKeyParser import dictionaryKeyParser
from src.helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ALGORITHM_choice) + '; e - EXIT: ').lower()
    if case == ALGORITHM_choice['RSA']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    elif case == ALGORITHM_choice['LRR']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    elif case == ALGORITHM_choice['ECDSA']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    if case == ALGORITHM_choice['EL_GAMAL']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    if case == ALGORITHM_choice['MD5']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    if case == ALGORITHM_choice['DH']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    if case == ALGORITHM_choice['ECDH']:
        __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
        deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Select algorithm.')
