1  parent = {}
2  
3  def DFS_Visit(Adj, s): 
4    for v in Adj[s]:
5      if v not in parent:
6        parent[v] = s
7        DFS_Visit(Adj, v) 
8  
9  def DFS(V, Adj):
10   for s in V:
11     if s not in parent:
12       parent[s] = None
13       DFS_Visit(Adj, s)
14 
15 vertices = ["a", "b", "c", "d", "e", "f"]
16 adjacency_list = {
17   "a": ["b", "d"],
18   "b": ["e"],
19   "c": ["e", "f"],
20   "d": ["b"],
21   "e": ["d"],
22   "f": ["f"]
23 }
24 
25 DFS(vertices, adjacency_list)
