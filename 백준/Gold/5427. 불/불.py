from collections import deque
def solution():
    w, h = map(int, input().split())
    building = [[] for _ in range(h)]
    fire = deque()
    for i in range(h):
        data = input()
        for j in range(w):
            if data[j] == '@': start = [i, j]
            if data[j] == '*': fire.append((i,j))
            building[i].append(data[j])


    def move_bfs(x, y):
        q = deque([(x,y)])
        visited[x][y] = 1
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1: return visited[cx][cy]
                if building[nx][ny] in '#': continue
                if fired[nx][ny] > 0 and fired[nx][ny] <= visited[cx][cy] + 1: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

        return -1

    def fire_bfs():
        while fire:
            cx, cy = fire.popleft()
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1: continue
                if building[nx][ny] in '#': continue
                if fired[nx][ny]: continue
                fired[nx][ny] = fired[cx][cy] + 1
                fire.append((nx, ny))


    visited = [[0] * w for _ in range(h)]
    fired = [[0] * w for _ in range(h)]
    for x, y in fire:
        fired[x][y] = 1
    fire_bfs()
    res = move_bfs(start[0], start[1])
    print("IMPOSSIBLE") if res < 0 else print(res)

test = int(input())
for t in range(test):
    solution()