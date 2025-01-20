from collections import deque
INF = int(1e9)
a, b, n, m = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs():
    q = deque([(n)])
    visited[n] = 0
    while q:
        cur = q.popleft()
        for next in (cur-1, cur+1, cur-a, cur-b, cur+a, cur+b, cur*a, cur*b):
            if next < 0 or next > 100000: continue
            if visited[next]: continue
            visited[next] = visited[cur] + 1
            q.append(next)
            if next == m: return visited[m]

print(bfs())