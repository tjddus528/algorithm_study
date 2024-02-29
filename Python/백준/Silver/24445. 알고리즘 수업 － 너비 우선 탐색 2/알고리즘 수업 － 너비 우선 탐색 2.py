from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
result = [0] * (n+1)
def bfs(start):
    cnt = 1
    q = deque([start])
    result[start] = cnt
    visited[start] = True
    while q:
        now = q.popleft()
        for next in sorted(graph[now], reverse = True):
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
                result[next] = cnt


bfs(r)
for i in range(1, n+1):
    print(result[i])