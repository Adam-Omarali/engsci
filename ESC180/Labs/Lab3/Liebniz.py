res = 0
# for i in range(1, 1000 + 1):
#     res += (((-1) ** (i % 2)) / i) * (2 * i) + 1

for i in range(0, 100000 + 1):
    res += (((-1) ** (i % 2)) / (2 * i + 1))

print(res * 4)
