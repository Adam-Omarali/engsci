from ll import Node, LL

def add_neighbours(node, neighbours):
    curr = node
    for neighbour in neighbours:
        curr.next = Node(neighbour)
        curr = curr.next
        
def get_neighbours(node, graph):
    curr = node.next
    neighbours = []
    while curr:
        neighbours.append(graph[curr.value - 1])
        curr = curr.next
        
    return neighbours
        

def graph():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    
    add_neighbours(one, [3, 6])
    add_neighbours(two, [3, 5])
    add_neighbours(three, [1, 2, 4, 5])
    add_neighbours(four, [3, 5])
    add_neighbours(five, [2, 4, 6])
    add_neighbours(six, [1, 5])
    
    adjacency = [one, two, three, four, five, six]
    return adjacency

def bfs(graph):
    visited = set()
    queue = [graph[0]]
    while len(queue) != 0:
        curr = queue.pop(0)
        print(curr.value)
        visited.add(curr)
        neighbours = get_neighbours(curr, graph)
        for neighbour in neighbours:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
        
        

def dfs(graph):
    visited = set()
    #FIFO
    stack = [graph[0]]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr.value)
            visited.add(curr)
            neighbours = get_neighbours(curr, graph)
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)
                        
    
g = graph()
print("bfs")
bfs(g)
print("dfs")
dfs(g)