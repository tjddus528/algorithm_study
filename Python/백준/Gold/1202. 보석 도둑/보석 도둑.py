import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewels = []
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))
bags = []
for i in range(k):
    bags.append(int(input()))

bags.sort()
result = 0
possible = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(possible, -heapq.heappop(jewels)[1])

    if possible:
        max_jewel = heapq.heappop(possible)
        result += -max_jewel
    elif not jewels:
        break


print(result)