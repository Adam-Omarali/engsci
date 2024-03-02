class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            print("Can't pop since stack is empty")
        else:
            return self.stack.pop()

s = Stack()
s.push(10)
s.push(20)
print(s.pop())
print(s.stack)

    