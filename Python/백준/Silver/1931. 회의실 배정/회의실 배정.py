import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for i in range(n):
    s, t = map(int, input().split())
    meetings.append((s,t))

meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
s = 0
for meet in meetings:
    if s <= meet[0]:
        count += 1
        s = meet[1]
print(count)