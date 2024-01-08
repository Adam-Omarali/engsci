import time
import matplotlib.pyplot as plt

#first one take longer since the function must be initialized
def time_func(f, x, n):
    s = 0
    for i in range(n):
        start = time.time()
        f(x)
        end = time.time()
        s += end - start
    
    s /= n

    return s


def counting_sort(L):
    values = [0] * (max(L) + 1)
    for e in L:
        values[e] += 1
    
    ret = []
    for i in range(len(values)):
        ret.extend([i] * values[i])
    
    return ret

def bubble_sort(L):
    for i in range(len(L)):
        swapped = False
        for j in range(len(L) - i - 1): #this works since after each iteration, the ith last element is in place
            if L[j] > L[j + 1]:
                L[j + 1], L[j] = L[j], L[j+1]
                swapped = True

        if not swapped:
            return L
    return L





L = [20, 30, 50, 50, 60, 10, 5, 2]
print(counting_sort(L))
print(bubble_sort(L))

ns = [1, 100, 10000]
counting_times = []
bubble_times = []
for n in ns:
    counting_times.append(time_func(counting_sort, L, n))
    bubble_times.append(time_func(bubble_sort, L, n))

plt.plot(ns, counting_times, label="counting")
plt.plot(ns, bubble_times, label="bubble")
plt.xlabel('input size')
plt.ylabel('runtime')
plt.legend(loc="upper left")
plt.show()