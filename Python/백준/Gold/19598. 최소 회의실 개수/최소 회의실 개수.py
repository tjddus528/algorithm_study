import heapq
import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for i in range(n):
    s, t = map(int, input().split())
    meetings.append((s,t))

meetings.sort(key = lambda x: x[0])

last = []
heapq.heappush(last, meetings[0][1])
for meet in meetings[1:]:
    start, end = meet[0], meet[1]
    min_end = heapq.heappop(last)
    if start < min_end:
        heapq.heappush(last, min_end)
    heapq.heappush(last, end)
print(len(last))