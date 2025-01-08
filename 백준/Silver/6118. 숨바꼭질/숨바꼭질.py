from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [int(1e9) for _ in range(n+1)]
distance[1] = 0

q = deque([1])
distance[1] = 0
while q:
    c = q.popleft()
    for v in graph[c]:
        if distance[v] <= distance[c] + 1: continue
        distance[v] = min(distance[c] + 1, distance[v])
        q.append(v)
max_dist = max(distance[1:])
cnt = distance[1:].count(max_dist)
for i in range(n+1):
    if distance[i] == max_dist:
        print(i, end=' ')
        break
print(max_dist, cnt)