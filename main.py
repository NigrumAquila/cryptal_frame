import core.encoding.toUTF8
from src.constants.algorithmConstants import ALGORITHM_choice
from core.constants.interfaceConstants import BACK, EXIT, ALGORITHM_MENU_MODULE_SPACE
from core.helpers.dictionaryHelpers import dictionaryKeyParser, dictionaryGetValueKeySeparated
from core.removers.removeModule import removeModule
from core.styles.colors import warning, end


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ALGORITHM_choice) + '; e - EXIT: ').lower()
    for alg in ALGORITHM_choice.keys():
        if case == ALGORITHM_choice[alg]:
            __import__(ALGORITHM_MENU_MODULE_SPACE + dictionaryKeyParser(ALGORITHM_choice, case))
            removeModule(dictionaryKeyParser(ALGORITHM_choice, case))
    
    if case == EXIT:
        end('Execution completed.')

    elif case not in ALGORITHM_choice.values():
        warning('Select algorithm.')