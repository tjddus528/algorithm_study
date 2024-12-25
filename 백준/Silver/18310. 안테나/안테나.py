import sys
input = sys.stdin.readline
n = int(input())        # ~ 200,000
houses = list(map(int, input().split()))

houses.sort()
min_index = (n-1)//2
print(houses[min_index])

