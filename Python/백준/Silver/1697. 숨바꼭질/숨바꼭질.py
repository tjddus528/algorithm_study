from collections import deque

n, k = map(int, input().split())

line = [0] * 100001
dx = [-1, 1]
def bfs(n):
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return
        for i in range(2):
            nx = x + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if line[nx] == 0:
                line[nx] = line[x] + 1
                q.append(nx)
            if nx == k:
                return
        if 2 * x <= 0 or 2 * x > 100000:
            continue
        if x != 0 and line[2*x] == 0:
            line[2*x] = line[x] + 1
            q.append(2 * x)
            if 2 * x == k:
                return


bfs(n)
print(line[k])
