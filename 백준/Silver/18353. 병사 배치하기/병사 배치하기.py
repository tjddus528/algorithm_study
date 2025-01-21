import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
length = [1 for _ in range(n)]
for k in range(n):
    for i in range(k):
        if data[i] > data[k]:
            length[k] = max(length[k], length[i]+1)

print(n - max(length))