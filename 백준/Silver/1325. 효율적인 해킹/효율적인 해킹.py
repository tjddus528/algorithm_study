from collections import deque
n, m = map(int, input().split())
computer = [[] for _ in range(n+1)]
hacking = []
for i in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)

max_cnt = 0
for idx in range(1, n+1):
    hacked = [0 for _ in range(n + 1)]
    cnt = 1
    q = deque([(idx)])
    hacked[idx] = 1
    while q:
        c = q.popleft()
        for next in computer[c]:
            if hacked[next]: continue
            hacked[next] = 1
            q.append(next)
            cnt += 1
    if max_cnt < cnt:
        hacking.clear()
        hacking.append(idx)
        max_cnt = cnt
    elif max_cnt == cnt: hacking.append(idx)

for h in sorted(hacking):
    print(h, end=' ')