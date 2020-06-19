def sqrtModP(number, modulo):
    assert number < modulo
    for candidate in range(1, modulo):
        if candidate * candidate % modulo == number:
            return (candidate, modulo - candidate)
        pass
    raise Exception('Point not found')

def power(x, y, p):
    res = 1  
    x = x % p
  
    while (y > 0):  
        if (y & 1): 
            res = (res * x) % p  
        y = y >> 1
        x = (x * x) % p  
    return res  
  
def squareRoot(n, p):
    if (p % 4 != 3) :
        return
    n = n % p  
    x = power(n, (p + 1) // 4, p)  
    if ((x * x) % p == n):
        return x
    x = p - x  
    if ((x * x) % p == n):
        return x