data = [list(map(int, input().split())) for _ in range(5)]
answer = set()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, number):
    if len(number) >= 6:
        answer.add(number)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > 4 or ny < 0 or ny > 4: continue
        number += str(data[nx][ny])
        dfs(nx, ny, number)
        number = number[:-1]

for i in range(5):
    for j in range(5):
        dfs(i, j, str(data[i][j]))

print(len(answer))