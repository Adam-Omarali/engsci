import time

def binary_search(L, e):
    low = 0
    high = len(L)-1
    while_count = 0
    while high-low >= 2:
        while_count += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid, while_count
        
    if L[low] == e:
        return low, while_count
    elif L[high] == e:
        return high, while_count
    else:
        return None, while_count
    
#Part A function works
# L = [x for x in range(0, 100, 10)]
# element = 30
# print(binary_search(L, element))

#always returns early (all elements are the same in L)
#never returns early (element is not in L, or element in smallest in L)

size = 100000
L = [x for x in range(0, size)]
element = (size - 1) // 2 #best case
element = size - 1 #worst case

start = time.time()
print(binary_search(L, element))
end = time.time()
print("Binary Search:", end - start)

start = time.time()
L.index(element)
end = time.time()
print("Linear Search:", end - start)