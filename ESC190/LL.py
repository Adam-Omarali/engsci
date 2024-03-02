class LL():
    def __init__(self):
        self.head = None #python will make any object.<attribute> exist, try f.head where f is a function

    def insert(self, loc, element):
        new_node = Node(element)
        if loc == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for i in range(loc - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def remove(self, loc):
        if loc == 0:
            self.head = self.head.next
        curr = self.head
        for i in range(loc - 1):
            curr = curr.next
        #skip the curr.next node
        #when an object is no longer reference in python, it is automatically freed
        curr.next = curr.next.next

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.stack = LL()

    #push: insert at 0
    def push(self, elem):
        self.stack.insert(0, elem)
        
    #pop: get 0 element and delete
    def pop(self):
        head = self.stack.head
        self.stack.remove(0)
        return head