from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
num = sorted(list(int(input()) for _ in range(n)))

def mode(num):
    num_cnt = Counter(num)
    max_cnt = max(num_cnt.values())
    res = []
    for nc in num_cnt:
        if num_cnt[nc]==max_cnt: res.append(nc)
    res.sort()
    return res[0] if len(res) <= 1 else res[1]

print(round(sum(num)/n))
print(num[(n-1)//2])
print(mode(num))
print(max(num)-min(num))