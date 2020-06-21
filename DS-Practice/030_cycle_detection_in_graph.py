
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Cycle Detection Program in Directed Connected Graph
'''

from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def detectCycles(self):
        visited = [False] * (self.vertices)
        recStack = [False] * (self.vertices)
        
        for node in range(self.vertices):
            if visited[node] == False:
                if(self.detectCycleUtil(node, visited, recStack) == True):
                    return True
        return False
        
    def detectCycleUtil(self, vertex, visited, recStack):
        
        visited[vertex] = True
        recStack[vertex] = True
        
        print(" ", vertex, end=" ")
        for neighbor in self.graph[vertex]:
            
            if visited[neighbor] == False:
                if(self.detectCycleUtil(neighbor, visited, recStack) == True):
                    return True 
                    
            elif(recStack[neighbor] == True):
                    return True
                   
        recStack[vertex] = False
        return False
        
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 1)
#g.add_edge(1, 4)
#g.add_edge(2, 3)
#g.add_edge(3, 3)
#g.add_edge(4, 2)

res = g.detectCycles()

if res:
    print("\nGraph has a cycle")
else:
    print("\nGraph does not contain a cycle")