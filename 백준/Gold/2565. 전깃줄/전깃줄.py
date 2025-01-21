import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a,b])
data.sort()
dp = [0 for _ in range(501)]
for a, b in data:
    dp[b] = max(dp[:b]) + 1
print(n-max(dp))