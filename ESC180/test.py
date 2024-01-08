def my_median(L):
  L = merge_sort(L)
  return L[(len(L) - 1) // 2]


def merge(L1, L2):
    if len(L1) == 0 and len(L2) == 0:
        return []
    elif len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    
    if L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    else:
        return [L2[0]] + merge(L1, L2[1:])

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    
    mid = len(L) // 2
    left_half = merge_sort(L[0:mid])
    right_half = merge_sort(L[mid:])
    return merge(left_half, right_half)

print(my_median([5.0, 2.0, 4.0, 1.0, 3.0]))