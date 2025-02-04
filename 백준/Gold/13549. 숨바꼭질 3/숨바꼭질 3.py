from collections import deque

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]

def bfs(n, k):
    visited[n] = 0
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k: return visited[now]
        if now*2 < 100001 and visited[now*2] <0:
            visited[now*2] = visited[now]
            q.append(now*2)
        if now-1 >=0 and visited[now-1] <0:
            visited[now-1] = visited[now] + 1
            q.append(now-1)
        if now+1 < 100001 and visited[now+1] <0:
            visited[now+1] = visited[now] + 1
            q.append(now+1)

    return -1

print(bfs(n, k))
