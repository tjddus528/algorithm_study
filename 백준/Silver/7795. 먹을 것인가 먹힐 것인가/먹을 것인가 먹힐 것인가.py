import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt, bidx = 0, 0
    for aa in a:
        while bidx < len(b):
            if aa <= b[bidx]: break
            bidx += 1
        cnt += bidx
    print(cnt)