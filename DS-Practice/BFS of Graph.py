
'''
C program link => https://www.thecrazyprogrammer.com/2015/09/breadth-first-search-bfs-program-in-c.html
'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Breadth First traversal for Graph
'''

from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def BFS(self, source):
        visited = [False] * (len(self.graph))
        
        visited[source] = True
        self.BFSutil(source, visited)
        
    def BFSutil(self, source, visited):
        
        queue = []
        queue.append(source)
        
        while(queue):
            vertex = queue.pop(0)

            print(" ", vertex, end=" ")
            
            for i in self.graph[vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)


print("BFS of Graph:")
g.BFS(0)
