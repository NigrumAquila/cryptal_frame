import src.helpers.encoding
from src.helpers.colors import warning, end
from src.helpers.constants import ALGORITHM_choice, BACK, EXIT, ALGORITHM_MENU_MODULE_SPACE
from src.helpers.deleteModuleIfReturn import deleteModuleIfReturn
from src.helpers.dictionaryKeyParser import dictionaryKeyParser
from src.helpers.dictionaryGetValueKeySeparated import dictionaryGetValueKeySeparated


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ALGORITHM_choice) + '; e - EXIT: ').lower()
    for alg in ALGORITHM_choice.keys():
        if case == ALGORITHM_choice[alg]:
            __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
            deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))
    
    if case == EXIT:
        end('Execution completed.')

    elif case not in ALGORITHM_choice.values():
        warning('Select algorithm.')

    # if case == ALGORITHM_choice['RSA']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['LRR']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['ECDSA']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['EL_GAMAL']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['MD5']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['DH']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['ECDH']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['EC_EL_GAMAL']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['AES']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['DES']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == ALGORITHM_choice['SHA256']:
    #     __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
    #     deleteModuleIfReturn(dictionaryKeyParser(ALGORITHM_choice, case))

    # elif case == EXIT:
    #     end('Execution completed.')

    # else:
    #     warning('Select algorithm.')
