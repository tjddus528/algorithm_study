import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
def draw(a,b,c,d, start):
    color = ['W', 'B']
    k = start
    count = 0
    for i in range(a,c):
        for j in range(b,d):
            if board[i][j] != color[k%2]:
                count += 1
            k += 1
        k += 1
    return count

result = 65
for i in range(n-7):
    for j in range(m-7):
        if i+8 > n or j+8 > m:
            continue
        result = min(result, draw(i, j, i+8, j+8, 0),draw(i, j, i+8, j+8, 1))

print(result)