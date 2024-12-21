from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

def melt():
    remain = 0
    checked = [[0]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if data[i][j] == 0: continue
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if data[ni][nj] == 0 and checked[ni][nj] == 0:
                    data[i][j] = max(data[i][j]-1, 0)
            checked[i][j] = 1
        remain += sum(data[i])
    if remain == 0: return True
    else: return False

def bfs(i, j, visited):
    q = deque([[i, j]])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1: continue
            if visited[nx][ny] or data[nx][ny] == 0: continue
            q.append([nx, ny])
            visited[nx][ny] = 1

def count():
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if visited[i][j] or data[i][j] == 0: continue
            bfs(i, j, visited)
            cnt += 1
    return cnt


year, melted = 0, False
while not melted:               # 다 녹았으면 종료
    if count() >= 2: break      # 1. 덩어리 수 세기
    melted = melt()             # 2. 빙산 녹이기 (다 녹았으면 True 반환)
    year += 1

print(year) if not melted else print(0)