import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = [[0]*w for _ in range(h)]

buildings = list(map(int, input().split()))


for j, bd in enumerate(buildings):
    for i in range(bd):
        arr[h-1-i][j] = 1


result = 0
for i in range(h-1, -1, -1):
    wall = False
    cnt = 0
    for j in range(w):
        if arr[i][j] == 1:  # 벽
            wall = True

        if wall:
            if arr[i][j] == 0:  # 빈 공간
                cnt += 1
            else:               # 벽
                result += cnt
                cnt = 0

print(result)