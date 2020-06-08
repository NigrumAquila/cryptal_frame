from ..common.multiplicativeInverse import multiplicativeInverse
from ..common.sqrtModP import sqrtModP, squareRoot
from ..helpers.fileHelpers import readParams
from ..helpers.constants import KEY_LENGTH_IN_BITS
from labmath import sqrtmod_prime
from random import randint

class EC():
    
    ZERO_POINT = {'x': 0, 'y': 0}

    params = {
        'a': int('340E7BE2A280EB74E2BE61BADA745D97E8F7C300', 16),
        'b': int('1E589A8595423412134FAA2DBDEC95C8D8675E58', 16),
        'modulo': int('E95E4A5F737059DC60DFC7AD95B3D8139515620F', 16),
        'x': int('BED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3', 16),
        'y': int('1667CB477A1A8EC338F94741669C976316DA6321', 16),
        'order': int('E95E4A5F737059DC60DF5991D45029409E60FC09', 16),
    }
    

    @staticmethod
    def generateKeys():
        params = readParams()
        privateKey = params.copy(); privateKey['d'] = randint(2**(KEY_LENGTH_IN_BITS-1), 2**KEY_LENGTH_IN_BITS)
        Q = EC.multiply({'x': params['x'], 'y': params['y']}, privateKey['d'])
        publicKey = params.copy(); publicKey['Qx'] = Q['x']; publicKey['Qy'] = Q['y']
        return {'public': publicKey, 'private': privateKey}


    @staticmethod
    def checkParams(params=params):
        assert 0 < params['a'] and params['a'] < params['modulo'] and 0 < params['b'] and params['b'] < params['modulo'] and params['modulo'] > 2
        assert (4 * (params['a'] ** 3) + 27 * (params['b'] ** 2))  % params['modulo'] != 0


    @staticmethod
    def validatePoint(point, params=params):
        if point == EC.ZERO_POINT: return True
        lhs, rhs = pow(point['y'], 2, params['modulo']), pow(pow(point['x'], 3) + params['a'] * point['x'] + params['b'], 1, params['modulo'])
        return lhs == rhs


    @staticmethod
    def findPointsOnX(x, params=params):
        assert x < params['modulo']
        left = (pow(x, 3) + params['a'] * x + params['b']) % params['modulo']
        leftSqrtModPrime = sqrtmod_prime(left, params['modulo'])
        coordsY = [params['modulo'] - leftSqrtModPrime, (params['modulo'] + leftSqrtModPrime) % params['modulo']]
        bottomY = min(coordsY); topY = max(coordsY)
        return {'bottom_point': {'x': x, 'y': bottomY}, 'high_point': {'x': x, 'y': topY}}


    reflectPoint = staticmethod(lambda point, params=params: {'x': point['x'], 'y': -point['y'] % params['modulo']})


    @staticmethod
    def addition(leftPoint, rightPoint, params=params):
        if leftPoint == EC.ZERO_POINT: return rightPoint
        if rightPoint == EC.ZERO_POINT: return leftPoint
        if leftPoint['x'] == rightPoint['x'] and (leftPoint['y'] != rightPoint['y'] or leftPoint['y'] == 0):
            return EC.ZERO_POINT
        if leftPoint['x'] == rightPoint['x']:
            left = (3 * leftPoint['x'] * leftPoint['x'] + params['a']) * multiplicativeInverse(2 * leftPoint['y'], params['modulo']) % params['modulo']
        else:
            left = (rightPoint['y'] - leftPoint['y']) * multiplicativeInverse(rightPoint['x'] - leftPoint['x'], params['modulo']) % params['modulo']
        x = (left * left - leftPoint['x'] - rightPoint['x']) % params['modulo']
        y = (left * (leftPoint['x'] - x) - leftPoint['y']) % params['modulo']
        return {'x': x, 'y': y}


    @staticmethod
    def multiply(point, factor, params=params):
        result = EC.ZERO_POINT
        m2 = point
        while 0 < factor:
            if factor & 1 == 1:
                result = EC.addition(result, m2, params)
            factor, m2 = factor >> 1, EC.addition(m2, m2, params)
        return result


    @staticmethod
    def getSubgroupOrder(generator={'x': params['x'], 'y': params['y']}, params=params):
        assert EC.validatePoint(generator, params) and generator != EC.ZERO_POINT
        for factor in range(1, params['modulo'] + 1):
            if EC.multiply(generator, factor, params) == EC.ZERO_POINT:
                return factor
        raise Exception("Invalid order")