from collections import deque
r, c = map(int, input().split())
S, water = deque(), deque()
data = [[] for _ in range(r)]
answer = [[0]*c for _ in range(r)]
for i in range(r):
    line = input()
    for j in range(c):
        if line[j] == 'S': S.append((i, j))
        if line[j] == '*': water.append((i, j))
        data[i].append(line[j])

visited = [[0]*c for _ in range(r)]
def bfs():
    while S:
        cx , cy = S.popleft()
        for dx, dy in ([-1, 0], [1, 0], [0, 1], [0, -1]):
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if visited[nx][ny]: continue
            if watered[nx][ny] and watered[nx][ny] <= visited[cx][cy] + 1: continue
            if data[nx][ny] == '*' or data[nx][ny] == 'X': continue
            visited[nx][ny] = visited[cx][cy] + 1
            if data[nx][ny] == 'D': return visited[nx][ny]
            S.append((nx, ny))
    return 0

watered = [[0]*c for _ in range(r)]
def flow():
    while water:
        x, y = water.popleft()
        for dx, dy in ([-1, 0], [0, -1], [0, 1], [1, 0]):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if watered[nx][ny]: continue
            if data[nx][ny] == 'X' or data[nx][ny] == 'D': continue
            watered[nx][ny] = watered[x][y] + 1
            water.append((nx, ny))

flow()
result = bfs()
if result > 0: print(result)
else: print("KAKTUS")