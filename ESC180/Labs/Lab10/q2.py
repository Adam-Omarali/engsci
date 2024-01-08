def times(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return -times(a, -b)
    
    return times(a, b-1) + a

print(times(-12, -3))


def linear_search(L, ans):
    if L[0] == ans:
        return 0
    
    return linear_search(L[1:], ans) + 1

L = [3, 4, 5, 10, 33, 2, 1]
print(linear_search(L, 33))

def interleave(L1, L2, final=None):
    #if you find your base case in len(list) = 1, the base case can be reduced further
    if len(L1) == 0:
        return []
    final = []
    final.append(L1[0])
    final.append(L2[0])
    final.extend(interleave(L1[1:], L2[1:]))
    return final # [L1[0], L2[0]] + interleave(L1[1:], L2[1:])


    if len(L1) == 0:
        # final.append(L1[0])
        # final.append(L2[0])
        return final
    
    final.append(L1[0])
    final.append(L2[0])
    interleave(L1[1:], L2[1:], final)
    return final

L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(interleave(L1, L2, []))



def f(L):
    ret = [2, 3]
    L[:] = ret

L1 = [1]
f(L1)
print(L1)


def reverse(L):
    if len(L) == 0:
        return []
    ret = []
    ret.append(L[-1])
    ret = ret + reverse(L[:-1])
    L = ret
    return ret

L = [1, 2, 3, 4, 5, 6]
print(reverse(L))
print("original L", L)

def reverse(L):
    reverse_inplace(L, 0)

def reverse_inplace(L, start):
    end = len(L) - start - 1
    # swap start and end
    if end > start:
        L[start], L[end] = L[end], L[start]
    
        reverse_inplace(L, start=start+1)

L = [1, 2, 3, 4, 5, 6]
reverse(L)
print("inplace", L)


def zigzag(L, i):
    n = len(L)
    if i == 1:
        print(L[n//2], end=" ")
    if n // 2 + i > len(L) - 1:
        print('')
    else:
        print(L[n // 2 - i], L[n // 2 + i], end=" ")
        zigzag(L, i + 1)

zigzag([1, 2, 3, 4, 5, 6, 7], 1)


def zigzag1(L):
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        zigzag1(L[1:-1]) # prints the inside elements
        print(L[0], L[-1], end = " ") # prints the outside elements

zigzag1([1, 2, 3, 4, 5, 6, 7])
