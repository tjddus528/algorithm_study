import sys
input = sys.stdin.readline

n = int(input())
data = []
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    total += b
    data.append((a,b))

data.sort()

people = 0
for d in data:
    people += d[1]
    if people >= total/2:
        print(d[0])
        break