class Queue:
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        self.start = 1
        self.end = 0
        self.size = size

    def enqueue(self, item):
        if self.end + 1 < self.size:
            self.end += 1
            #what if self.start at 0?
        else:
            self.end = 0
        
        self.data[self.end] = item


    def dequeue(self):
        ret_val = self.data[self.start]
        self.data[self.start] = None
        if self.start + 1 < self.size:
            self.start += 1
        else:
            self.start = 0

        return ret_val 

    def __str__(self):
        return str(self.data) + ", Start:" + str(self.start) + ", End:" + str(self.end) 

    def __repr__(self):
        string = ""
        start = self.start
        while (start != self.end):
            string += str(self.data[start]) + "->"
            if (start + 1 < self.size):
                start += 1
            else:
                start = 0
        string += str(self.data[self.end])
        return string
    
    #if same size, one with less elements comes first
    def __lt__(self, other):
        self_start = self.start
        other_start = other.start
        while (self_start != self.end and other_start != other.end):
            if (self.data[self_start] < other.data[other_start]):
                #self comes first
                return True
            elif (self.data[self_start] > other.data[other_start]):
                #other comes first
                return False
            else:
                if (self_start + 1 < self.size):
                    self_start += 1
                else:
                    self_start = 0  

                if (other_start + 1 < other.size):
                    other_start += 1
                else:
                    other_start = 0 
        
        return self.size < other.size
    
    # def sort_queues(self, others):
    #     others.append(self)
    #     for i in range(len(others)):
    #         for j in range(1, len(others)):
    #             if (others[i] < others[j]):
    #                 temp = others[i]
    #                 others[i] = others[j]
    #                 others[j] = temp
        
    #     for i in range(len(others)):
    #         others[i].__printseq__()

    # def __repr__(self):
    #     print(self.data, ", Start:", self.start, ", End:", self.end)