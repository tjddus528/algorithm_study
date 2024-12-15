import sys
input = sys.stdin.readline

point = []
n = int(input())
for _ in range(n):
    point.append(list(map(int, input().split())))

point.sort(key = lambda p: (p[0], p[1]))
for x, y in point:
    print(x, y)