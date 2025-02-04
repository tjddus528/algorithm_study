import sys
input = sys.stdin.readline
m = int(input())
s = 0
for _ in range(m):
    data = input().strip().split()
    if data[0]=="all":
        s = (1 << 21) -1
        continue

    if data[0]=="empty":
        s = 0
        continue

    x = int(data[1])
    if data[0]=="add":
        s |= (1 << x)
        continue

    if data[0]=="remove":
        s &= ~(1 << x)
        continue

    if data[0]=="check":
        print(1 if s & (1 << x) !=0 else 0)
        continue

    if data[0]=="toggle":
        s ^= (1 << x)
        continue
