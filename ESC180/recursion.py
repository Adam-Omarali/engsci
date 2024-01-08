def multiply(n, m):
    if n == 0:
        return 0
    return (n - 1) * m + m


def pow(base, exp):
    if exp == 0:
        return 1
    
    return base * pow(base, exp - 1)


def count_down(n):
    if n == 0:
        print(0)
        return
    
    print(n)
    return count_down(n - 1)

def count_up(n):
    if n == 0:
        print(0)
        return 0
    
    res = count_up(n - 1)
    print(n - res)
    return res

def reverse(s):
    if len(s) == 0:
        return ''
    
    return s[-1] + reverse(s[:-1])

def check_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if (i * i) > n:
        return True
    
    
    return check_prime(n, i + 1) 



def fib_n(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib_n(n-1) + fib_n(n - 2)