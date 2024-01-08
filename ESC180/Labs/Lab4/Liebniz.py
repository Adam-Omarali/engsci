import math

# res = 0
# for i in range(1, 1000 + 1):
#     res += (((-1) ** (i % 2)) / i) * (2 * i) + 1

# for i in range(0, 100000 + 1):
#     res += (((-1) ** (i % 2)) / (2 * i + 1))


count = 0
res = 0
while count < 120:
    res += (((-1) ** (count % 2)) / (2 * count + 1))
    count += 1




def approxPi(sigfigs):
    compare = int(math.pi * (10 ** (sigfigs - 1)))
    res = 0
    i = 0
    while int(res * 4 * (10 ** (sigfigs - 1))) != compare:
        res += (((-1) ** (i % 2)) / (2 * i + 1))
        i += 1

    print(res * 4)
    return i
    
if __name__ == '__main__':
    count = 0
    res = 0
    while count < 120:
        res += (((-1) ** (count % 2)) / (2 * count + 1))
        count += 1
    print(res * 4)
    print(approxPi(3))