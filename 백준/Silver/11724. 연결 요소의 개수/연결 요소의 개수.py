import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(n+1)]
def dfs(start):
    visited[start] = 1
    for g in graph[start]:
        if not visited[g]:
            dfs(g)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)