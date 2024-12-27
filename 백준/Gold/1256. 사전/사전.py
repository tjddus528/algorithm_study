from itertools import combinations
import sys
sys.setrecursionlimit(10**9)
n, m, k = map(int, input().split())
dp = [[1]*(m+1) for _ in range(n+1)]

dp[0][1] = 1
dp[1][0] = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

str = ''
i, j = n, m
while i > 0 and j > 0:
    if dp[i-1][j] >= k:
        str += 'a'
        i -= 1
    else:
        str += 'z'
        k -= dp[i-1][j]
        j -= 1
else:
    str += 'a'*i + 'z'* j

print(str if k <= 1 else -1)