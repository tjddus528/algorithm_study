n, m = map(int, input().split())
data = list(list(int(i) for i in input()) for _ in range(n))
square = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        square[i][j] = sum(sum(item) for item in [data[k][:j+1] for k in range(i+1)])

answer = 0
# 1.
for i in range(n):
    for j in range(m):
        a = square[i][j]
        b = square[i][m-1] - square[i][j]
        c = square[n-1][j] - square[i][j]
        d = square[n-1][m-1] - (square[n-1][j] + square[i][m-1]) + square[i][j]
        answer = max(answer, max(a * b * (c + d), a * c * (b + d), (a + b) * c * d, (a + c) * b * d))

# 2. 세로
for j in range(m):
    for jj in range(j+1, m):
        a = square[n-1][j]
        b = square[n-1][jj] - a
        c = square[n-1][m-1] - a - b
        answer = max(answer, a * b * c)
# 3. 가로
for i in range(n):
    for ii in range(i+1, n):
        a = square[i][m-1]
        b = square[ii][m-1] - a
        c = square[n-1][m-1] - a - b
        answer = max(answer, a * b * c)

print(answer)