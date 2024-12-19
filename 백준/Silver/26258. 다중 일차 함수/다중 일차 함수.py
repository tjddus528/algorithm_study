import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
k = list([i, float(input())] for i in range(q))
k.sort(key=lambda x:x[1])

i, j = 0, 0
while i < n and j < q:
    while float(data[i][0]) <= k[j][1]:
        i += 1
    if data[i][1] > data[i-1][1]: k[j].append(1)
    elif data[i][1] < data[i-1][1]: k[j].append(-1)
    else: k[j].append(0)
    j += 1
k.sort(key=lambda x:x[0])
for kk in k: print(kk[2])