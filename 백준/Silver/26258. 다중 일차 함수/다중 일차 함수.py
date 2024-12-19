import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

def solution(k):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right)//2
        if float(data[mid][0]) > k: right = mid -1
        else: left = mid + 1

    if data[left][1] > data[left-1][1]: return 1
    elif data[left][1] < data[left-1][1]: return -1
    else: return 0

q = int(input())
for _ in range(q):
    print(solution(float(input())))
