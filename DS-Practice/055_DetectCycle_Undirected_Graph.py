
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

def detectCycleUtil(g, v, visited, parent):
    visited[v] = True
    for i in g.graph[v]:
        if visited[i] == False:
            if detectCycleUtil(g, i, visited, v):
                return True
        elif parent != i:
            return True
    return False

def detectCycle(g):
    visited = [False] * g.vertices
    for i in range(g.vertices):
        if visited[i] == False:
            if detectCycleUtil(g, i, visited, -1):
                return True
    return False

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)

isCycle = detectCycle(g)
if isCycle:
    print("Graph contains cycle")
else: 
    print("Graph does not contain cycle")
