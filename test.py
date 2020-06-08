without_keys = lambda dictionary, keys: {key: value for key, value in dictionary.items() if key not in keys}

ALGORITHM_choice = {
    'RSA': '1',
    'LRR': '2',
    'ECDSA': '3',
    'EL_GAMAL': '4',
    'MD5': '5',
}

dictionaryGetValueKey = lambda dictionary: [value + ' - ' +key for key, value in dictionary.items()]

getAlgorithmsSeparated = lambda dictionary: '; '.join(dictionaryGetValueKey(dictionary))


print(getAlgorithmsSeparated(ALGORITHM_choice))