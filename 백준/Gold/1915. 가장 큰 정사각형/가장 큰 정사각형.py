n, m = map(int, input().split())
arr = list(list(int(i) for i in input()) for _ in range(n))
dp = [[0 for _ in range(m)] for _ in range(n)]

result = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            continue
        else:
            a = (0 if y < 1 else dp[x][y-1]) + arr[x][y]
            b = (0 if x < 1 else dp[x-1][y]) + arr[x][y]
            c = (0 if (x < 1 or y < 1) else dp[x-1][y-1]) + arr[x][y]
            dp[x][y] = min(a,b,min(a, b, c))
            result = max(result, dp[x][y])

print(result**2)
