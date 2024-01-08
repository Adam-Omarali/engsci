def gcd(n, m):
    global divisor
    topRange = min(n, m)
    for i in range(topRange, 1, -1):
        if(n % i == 0 and m % i == 0):
            return i

if __name__ == '__main__':
    divisor = 1
    print(gcd(34, 17))