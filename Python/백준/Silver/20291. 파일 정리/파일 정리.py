from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
files = []
for _ in range(n):
    name, file = input().rstrip().split('.')
    files.append(file)
files.sort()

data = Counter(files)
for d in data:
    print(d, data[d])


