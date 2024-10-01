class MinHeap():
    def __init__(self):
        self.heap = [None]   
        self.curr = 0
        
    def insert(self, elem):
        priority = elem[0]
        
        self.curr += 1
        idx = self.curr
        self.heap.append(elem)
        while idx > 1 and self.heap[idx // 2][0] > priority:
            self.heap[idx] = self.heap[idx // 2]
            self.heap[idx // 2] = elem
            idx //= 2
                    
    def extract_min(self):
        ret = self.heap[1]
        self.heap[1] = self.heap[self.curr]
        self.curr -= 1
        #check both right and left, swap with the larger one since mean heap
        level = 1
        while (2 * level <= self.curr):
            next_level = 2 * level
            if (next_level <= self.curr and self.heap[next_level][0] > self.heap[next_level + 1][0]):
                next_level += 1
            if self.heap[level][0] <= self.heap[next_level][0]:
                break
            
            temp = self.heap[next_level]
            self.heap[next_level] = self.heap[level]
            self.heap[level] = temp
            level = next_level
        return ret
    
    

h = MinHeap()
h.insert((5, "a"))
h.insert((2, "b"))
h.insert((3, "c"))
print(h.extract_min()) # "b"
print(h.extract_min()) # "c"
print(h.extract_min()) # "a"       
        
        
    