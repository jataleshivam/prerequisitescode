import sys
sys.setrecursionlimit(10**7)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    stack.append(u)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    stack = []
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    
    print(*reversed(stack))