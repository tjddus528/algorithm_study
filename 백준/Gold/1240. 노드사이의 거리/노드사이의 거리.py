n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(m):
    u, v = map(int, input().split())
    visited = [0 for _ in range(n + 1)]
    result = []
    def dfs(start, target, dist):
        visited[start] = 1
        if start == target:
            result.append(dist)
            return
        for v, w in graph[start]:
            if visited[v]: continue
            dfs(v, target, dist + w)

    dfs(u, v, 0)
    print(min(result))