n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
dp = [[0]*n for _ in range(n)]
dp[0][0] = data[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + data[i][0]
result = dp[0][0]
for i in range(1, n):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]
    result = max(max(dp[i]), result)
print(result)