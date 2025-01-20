from collections import deque
INF = int(1e9)
a, b, n, m = map(int, input().split())
d = [INF for _ in range(100001)]
visited = [0 for _ in range(100001)]

def bfs():
    q = deque([(n)])
    d[n] = 0
    while q:
        cur = q.popleft()
        for gap in (-1, 1, -a, -b, +a, +b):
            next = cur + gap
            if next < 0 or next > 100000: continue
            if visited[next]: continue
            d[next] = d[cur]+1
            visited[next] = 1
            q.append(next)
            if next == m:
                return
        for multi in (a, b):
            next = cur * multi
            if next < 0 or next > 100000: continue
            if visited[next]: continue
            d[next] = d[cur] + 1
            visited[next] = 1
            q.append(next)
            if next == m:
                return

bfs()
print(d[m])
