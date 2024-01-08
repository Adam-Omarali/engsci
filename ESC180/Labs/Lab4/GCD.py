def badGCD(n, m):
    topRange = min(n, m)
    ret = 1
    for i in range(1, topRange + 1):
        if(n % i == 0 and m % i == 0):
            ret = i

    return ret

def gcd(n, m):
    topRange = min(n, m)
    divisor = topRange
    while divisor > 0:
        if (n % divisor == 0 and m % divisor == 0):
            return divisor
        divisor -= 1

    # for i in range(topRange, 1, -1):
    #     if(n % i == 0 and m % i == 0):
    #         return i

def simplify_fraction(n, m):
    divisor = gcd(n, m)
    numerator = n // divisor
    denominator = m // divisor
    if(denominator == 1):
        return str(numerator)
    else:
        return str(numerator) + "/" + str(denominator)
        
if __name__ == '__main__':
    print(badGCD(34, 17))
    print(gcd(34, 17))
    print(simplify_fraction(8, 4))