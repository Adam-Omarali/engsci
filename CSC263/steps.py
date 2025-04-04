import numpy as np

class Node():
    def __init__(self, adj):
        self.adj = adj
        self.color = 'w'
        self.d = np.inf
        self.parent = None

def BFS(N, X, Y, U, D):
    G = {}
    for floor in range(1, N+1):
        neighbours = []
        if floor + U <= N:
            neighbours.append(floor + U)
        if floor - D > 0:
            neighbours.append(floor - D)
            
        
        G[floor] = Node(neighbours)
        
    G[X].color = 'g'
    G[X].d = 0
    
    queue = [X]
    while len(queue) > 0:
        curr = queue.pop()
        if curr == Y:
            # return G[curr].d
            path = []
            curr_node = G[curr]
            while curr_node.parent != None:
                path.append(curr)
                curr = curr_node.parent
                curr_node = G[curr]
            path.append(X)
            path.reverse()
            return path
                
        else:
            for e in G[curr].adj:
                if (G[e].color == 'w'):
                    G[e].color = 'g'
                    G[e].d = G[curr].d + 1
                    G[e].parent = curr
                    queue.append(e)

            
    return "take the stairs"

print(BFS(10, 1, 10, 2, 1))