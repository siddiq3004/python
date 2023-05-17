# The DFS algorithm is a recursive algorithm that uses the idea of backtracking.
from collections import defaultdict
class graph:
    def __init__(self):
        self.graph  = defaultdict(list)
    # function to add edges
    def addEdge(self,u , v):
        self.graph[u].append(v)
    # function used by DFS
    def DFSutil(self,v,visited):
        visited.add(v)
        print(v,end="")
        for i in self.graph[v]:
            # print('i',i)
            if i not in visited:
                self.DFSutil(i,visited)
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        visited = set()
        # self.DFSutil(v,visited)
        # call the recursive helper function to print DFS traversal starting from all
    # vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSutil(vertex, visited)
if __name__ == "__main__":
    g = graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
print(g.graph)
g.DFS()
# -------------------------------------------------
# def dfsOfGraph(self, V, adj):
#         # code here
#         visited=[0]*V
#         values=[]
#         self.dfs(0,adj,visited,values)
#         return values
#     def dfs(self,node,adj,visited,values):
#         visited[node]=1
#         values.append(node)
#         for i in adj[node]:
#             if visited[i]==0:
#                 self.dfs(i,adj,visited,values)

