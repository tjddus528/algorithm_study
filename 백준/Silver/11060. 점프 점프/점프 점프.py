n = int(input())
data = list(map(int, input().split()))
dp = [0] + [int(1e9)]*(n-1)

for i in range(n):
    for j in range(1, data[i]+1):
        if i+j >= n: break
        dp[i+j] = min(dp[i] + 1, dp[i+j])
print(dp[n-1]) if dp[n-1] < int(1e9) else print(-1)