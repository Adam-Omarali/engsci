def changeRow(L):
    x = L[:]
    x[0] = [3, 2, 1]
    print(x)

L = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

changeRow(L)
print(L)