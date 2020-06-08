ASSYMETRIC_ALGORITHMS = ['RSA', 'EC', 'EL_GAMAL', 'DH']

alg = 'DH'

if alg in ASSYMETRIC_ALGORITHMS and alg not in ['DH', 'EC']:
    print(alg)