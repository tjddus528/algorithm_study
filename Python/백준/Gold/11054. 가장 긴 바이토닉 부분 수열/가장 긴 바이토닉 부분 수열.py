import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reverse = arr[::-1]

asc_dp = [1] * n
desc_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            asc_dp[i] = max(asc_dp[j] + 1, asc_dp[i])
        if reverse[i] > reverse[j]:
            desc_dp[i] = max(desc_dp[j]+1, desc_dp[i])

result = [0 for i in range(n)]
for i in range(n):
    result[i] = asc_dp[i] + desc_dp[n-1-i] -1
print(max(result))