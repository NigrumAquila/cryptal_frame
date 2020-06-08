without_keys = lambda dictionary, keys: {key: value for key, value in dictionary.items() if key not in keys}

ALGORITHM_choice = {
    'RSA': '1',
    'LRR': '2',
    'ECDSA': '3',
    'EL_GAMAL': '4',
    'MD5': '5',
}

print(without_keys(ALGORITHM_choice, 'RSA'))