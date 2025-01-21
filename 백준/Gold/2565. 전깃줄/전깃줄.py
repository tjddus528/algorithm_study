import sys
input = sys.stdin.readline
n = int(input())
data = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0 for _ in range(501)]
for a, b in data:
    dp[b] = max(dp[:b]) + 1
print(n-max(dp))