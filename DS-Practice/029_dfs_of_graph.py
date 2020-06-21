
'''
C Program Link => https://www.thecrazyprogrammer.com/2014/03/depth-first-search-dfs-traversal-of-a-graph.html
'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def DFS(self, source):
        visited = [False] * (len(self.graph))
        
        self.DFSutil(source, visited)
        
    def DFSutil(self, source, visited):
        
        visited[source] = True
        print(" ", source, end=" ")
        
        for i in self.graph[source]:
            if visited[i] == False:
                self.DFSutil(i, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 4)


print("DFS of Graph:")
g.DFS(0)
