import sys
input = sys.stdin.readline
n, c = map(int, input().split())
w = list(map(int, input().split()))
w.sort()

def bs(target):
    min, max = 0, len(w)-1
    while min <= max:
        mid = (min + max) // 2
        if w[mid] == target: return 1
        elif w[mid] > target: max = mid - 1
        else: min = mid + 1
    return 0

def solution(n, c, w):
    if bs(c): return 1

    a, b = 0, len(w)-1
    while a < b:
        total = w[a] + w[b]
        if total == c: return 1
        elif total > c: b -= 1
        else:
            diff = c - total
            if w[a] != diff and w[b] != diff and bs(diff): return 1
            a += 1
    return 0

print(solution(n, c, w))