import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
data = []
tomato = deque()
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 1:
            tomato.append((i, j))


def is_ripe(data):
    global step
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                return False
        step = max(step, max(data[i]))

    return True


step = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while tomato:
    x, y = tomato.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue
        if data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            tomato.append((nx, ny))


if is_ripe(data):
    print(step-1)
else:
    print(-1)
