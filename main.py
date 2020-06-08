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

    elif case == EXIT:
        end('Execution completed.')

    else:
        warning('Select algorithm.')
