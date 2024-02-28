from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    cx, cy = 2*characterX, 2*characterY
    ix, iy = 2*itemX, 2*itemY
    board = [[-1]*102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]
    # draw
    for r in rectangle:
        a, b, c, d = map(lambda x: x*2, r)
        for x in range(a, c+1):
            for y in range(b, d+1):
                if a < x < c and b < y < d:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # bfs
    q = deque()
    q.append((cx, cy))
    visited[cx][cy] = 0
    while q:
        x, y = q.popleft()
        if x == ix and y == iy:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx < 0 or nx > 102 or ny < 0 or ny > 102:
                continue
            if board[nx][ny] == 1:
                if visited[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    
    return answer