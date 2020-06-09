from .dictionaryWithoutKeys import dictionaryWithoutKeys


EXIT = 'e'
BACK = 'b'
KEY_LENGTH_IN_BYTES = 16
KEY_LENGTH_IN_BITS = KEY_LENGTH_IN_BYTES*8
ALGORITHM_MENU_MODULE_SPACE = 'src.algorithms_menu.menu_'

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
}

ENCRYPTION_ALGORITHMS = dictionaryWithoutKeys(ALGORITHM_choice, ['MD5', 'SHA256'])
HASH_FUNCTIONS = {'MD5', 'SHA256'}
ASSYMETRIC_ALGORITHMS = ['RSA', 'ECDSA', 'EL_GAMAL', 'DH', 'ECDH', 'EC_EL_GAMAL']

RSA_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'ENCRYPT_FILE': '4',
    'DECRYPT_FILE': '5',   
}

LRR_choice = {
    'GENERATE_KEY': '1',
    'SELECT_KEY': '2',
    'ENCRYPT_FILE': '3',
    'DECRYPT_FILE': '4',
}

ECDSA_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'SIGN_FILE': '4',
    'VERIFY_FILE': '5',
}

EL_GAMAL_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'ENCRYPT_FILE': '4',
    'DECRYPT_FILE': '5',
}

MD5_choice = {
    'GENERATE_DIGEST': '1',
}

DH_choice = {
    'GENERATE_SECRET': '1',
}

ECDH_choice = {
    'GENERATE_SECRET': '1',
}

EC_EL_GAMAL_choice = {
    'GENERATE_KEYS': '1',
    'GENERATE_POINT': '2',
    'SELECT_PUBLIC_KEY': '3',
    'SELECT_PRIVATE_KEY': '4',
    'ENCRYPT_POINT': '5',
    'DECRYPT_POINT': '6',
}

AES_choice = {
    'GENERATE_KEY': '1',
    'SELECT_KEY': '2',
    'ENCRYPT_FILE': '3',
    'DECRYPT_FILE': '4',
}

DES_choice = {
    'GENERATE_KEY': '1',
    'SELECT_KEY': '2',
    'ENCRYPT_FILE': '3',
    'DECRYPT_FILE': '4',
}

SHA256_choice = {
    'GENERATE_DIGEST': '1',
}