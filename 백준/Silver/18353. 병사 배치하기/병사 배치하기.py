import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

def bs(l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] > target: l=mid+1
        else: r=mid-1
    return l

cnt = 0
i, j = 1, 0
lst = [0 for _ in range(n)]
lst[0] = data[0]
while i < n:
    if lst[j] > data[i]:
        lst[j+1] = data[i]
        j += 1
    else:
        idx = bs(0, j, data[i])
        lst[idx] = data[i]
        cnt += 1
    i += 1

print(cnt)