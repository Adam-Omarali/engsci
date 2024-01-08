def get_nums(L):
    ret = []
    for i in range(len(L)):
        ret.append(L[i][1])

    return ret

def lookup(L, num):
    for i  in range(len(L)):
        if L[i][1] == num:
            return L[i][0]
    
    return None


L = [["CIV", 92], ["180", 98], ["103", 99], ["194", 95]]

print(L[2][1]) #99
print(get_nums(L)) #[92, 98, 99, 95]
print(lookup(L, 99)) #103
