from ll import Node, LL
# 1 -> 2 -> 3
# 2 -> 5
# 3 -> 4
# 4 ->
# 5 ->

def construct_adjacency_list():
    one = Node(1) 
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    
    one.next = Node(2)
    one.next.next = Node(3)
    two.next = Node(5)
    three.next = Node(4)
    
    adjacency = [one, two, three, four, five]
    return adjacency
    
def are_linked(node1, node2):
    while node1 != None:
        if node1.value == node2.value:
            return True
        node1 = node1.next
    return False


graph = construct_adjacency_list()
print(are_linked(graph[0], graph[4]))
    
    
    