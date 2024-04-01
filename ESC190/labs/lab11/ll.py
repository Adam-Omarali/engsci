class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LL():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next