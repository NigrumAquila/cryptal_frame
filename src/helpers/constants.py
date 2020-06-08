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
}

ASSYMETRIC_ALGORITHMS = ['RSA', 'EC', 'EL_GAMAL']

RSA_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'ENCRYPT_FILE': '4',
    'DECRYPT_FILE': '5'    
}

LRR_choice = {
    'GENERATE_KEY': '1',
    'SELECT_KEY': '2',
    'ENCRYPT_FILE': '3',
    'DECRYPT_FILE': '4'
}

ECDSA_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'SIGN_FILE': '4',
    'VALIDATE_FILE': '5'
}

# ECC_choice = {
#     'GENERATE_KEYS': '1',
#     'SELECT_PUBLIC_KEY': '2',
#     'SELECT_PRIVATE_KEY': '3',
#     'ENCRYPT_FILE': '4',
#     'DECRYPT_FILE': '5'
# }

EL_GAMAL_choice = {
    'GENERATE_KEYS': '1',
    'SELECT_PUBLIC_KEY': '2',
    'SELECT_PRIVATE_KEY': '3',
    'ENCRYPT_FILE': '4',
    'DECRYPT_FILE': '5'
}