# from sympy import randprime, primitive_root
# from random import randint

# p = randprime(2**127, 2**128)
# g = primitive_root(p)
# # g = getPrimitiveRoot(p)
# x = randint(1, p-1)
# y = pow(g, x, p)

# print(x.to_bytes(16, byteorder='big'))
# print(y.to_bytes(16, byteorder='big'))


from src.helpers.fileHelpers import readKey

print(readKey('EL_GAMAL'))