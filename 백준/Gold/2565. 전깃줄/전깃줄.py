import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a,b])

data.sort()

def bs(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < target: left = mid + 1
        else: right = mid
    return right
cnt = 0
i, j = 1, 0
lst = [0 for _ in range(n)]
lst[0] = data[0][1]
while i < n:
    if lst[j] < data[i][1]:
        lst[j+1] = data[i][1]
        j += 1
    else:
        idx = bs(0, j, data[i][1])
        lst[idx] = data[i][1]
        cnt += 1
    i += 1

print(cnt)