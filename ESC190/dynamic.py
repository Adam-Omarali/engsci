#this is O(n) since there are n additions as each fib(n) is only computed once
#for space complexity, the numbers grow so fast that the couple number makes the previous number
def fib(n, m={0: 1, 1:1}):
    if n in m:
        return m[n]
    m[n] = fib(n-1, m) + fib(n-2, m)
    return m[n]

#space complexity
#fib n ~ phi^n / sqrt(5), where phi is the golden ratio
#number of digits in fib n is log(fib n) ~ n log(phi) - log(5)/2
#log phi * (1 + 2 + 3 + ... + n) - log 5/2 * n
#log phi * n(n+1)/2 - log 5/2 * n
#O(n^2)

print(fib(4))

#building up from small problems
def fib_dynamic(n):
    fib_start = [0]*(n+1)
    fib_start[0] = fib_start[1] = 1
    for i in range(2, n+1):
        fib_start[i] = (fib_start[i-1] + fib_start[i-2])
    return fib_start[n]

print(fib_dynamic(4))