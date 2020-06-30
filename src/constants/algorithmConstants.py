from core.helpers.dictionaryHelpers import dictionaryWithoutKeys

ALGORITHM_choice = {
    'RSA': '1',
    'LRR': '2',
    'ECDSA': '3',
    'EL_GAMAL': '4',
    'MD5': '5',
    'DH': '6',
    'ECDH': '7',
    'EC_EL_GAMAL': '8',
    'AES': '9',
    'DES': '10',
    'SHA256': '11',
    'DSA': '12',
    'EL_GAMAL_SIGNATURE_SCHEME': '13',
}

ENCRYPTION_ALGORITHMS = dictionaryWithoutKeys(ALGORITHM_choice, ['MD5', 'SHA256'])
HASH_FUNCTIONS = {'MD5', 'SHA256'}
ASSYMETRIC_ALGORITHMS = ['RSA', 'ECDSA', 'EL_GAMAL', 'DH', 'ECDH', 'EC_EL_GAMAL', 'DSA', 'EL_GAMAL_SIGNATURE_SCHEME']

