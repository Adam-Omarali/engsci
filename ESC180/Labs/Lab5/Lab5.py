def count_evens(L):
    count = 0
    for i in L:
        if i % 2 == 0:
            count += 1
    
    return count

def list_to_str(L):
    ret = "'["
    for i in L:
        ret += str(i) + ', '
    
    #this doesn't work for an empty list, so you need to add a condition here or in the for loop
    if(len(L) > 0):
        ret = ret[:-2]
    ret += "]'"
    return ret

def lists_are_the_same(L1, L2):
    if(len(L1) == len(L2)):
        for i in range(len(L1)):
            if L1[i] == L2[i]:
                continue
            else:
                return False
        return True
    
    return False

def list1_start_with_list2(L1, L2):
    if len(L1) >= len(L2):
        for i in range(len(L2)):
            if L1[i] == L2[i]:
                continue
            else:
                return False
        return True
    return False

def match_pattern(L1, L2):
    for j in range(len(L1) - len(L2) + 1):
        subL1 = L1[j:j + len(L2)] #list slicing doesn't go out of bounds, but this would check extra without the end condition for the for loop
        print(subL1)
        if (subL1 == L2):
            return True
    return False

def duplicates(L1):
    for i in range(1, len(L1)):
        #no need to check multiple at once i-1 and i + 1, that actually does extra checks
        if L1[i - 1] == L1[i]:
            return True
        
    return False

l1 = [1, 2, 3, 4]
l2 = [1, 4, 3]
print(count_evens(l1))
print(list_to_str([]))
print(lists_are_the_same(l1, l2))
print(list1_start_with_list2(l1, l2))
print(match_pattern(l1, l2))
print(duplicates([0, 1, 2, 4, 3]))
