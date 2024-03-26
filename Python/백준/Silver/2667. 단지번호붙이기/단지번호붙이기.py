from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
maps = []
for _ in range(n):
    maps.append(input().rstrip())

visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(sx, sy):
    count = 1
    visited[sx][sy] = True
    q = deque()
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == '1':
                visited[nx][ny] = True
                count += 1
                q.append((nx,ny))
    return count

answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == '1':
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for asw in answer:
    print(asw)