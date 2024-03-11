#FIFO: First in first out
class Queue():
    def __init__(self):
        self.queue = []
    
    #add an object to the front of the queue
    def enqueue(self, elem):
        self.queue.insert(0, elem) #O(n) complexity

    #remove and return the last element in the queue
    def dequeue(self):
        return self.queue.pop() #O(1) complexity, specifying an index would be an O(n) operation sinc eyou have to shift everything
        #after what's popped forward one index
    
    def __str__(self):
        return str(self.queue)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)