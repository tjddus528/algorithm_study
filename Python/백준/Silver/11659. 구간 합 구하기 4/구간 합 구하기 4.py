import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = [0] * n
total[0] = arr[0]
for i in range(1, n):
    total[i] = total[i-1] + arr[i]

for _ in range(m):
    i, j = map(int, input().split())
    res = total[j-1]
    if i != 1:
        res -= total[i-2]
    print(res)
