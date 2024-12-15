import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt = 0
    for aa in a:
        left, right = 0, len(b)-1
        while left <= right:
            mid = (left + right) // 2
            if aa <= b[mid]: right = mid - 1
            elif aa > b[mid]: left = mid + 1
        cnt += len(b[:left])
    print(cnt)