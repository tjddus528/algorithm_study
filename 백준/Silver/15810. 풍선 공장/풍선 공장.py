n, m = map(int, input().split())
staff = list(map(int, input().split()))
staff.sort()

def balloon(time):
    cnt = 0
    for st in staff:
        cnt += time // st
    return cnt

maxt = staff[0] * m
mint = 1
res = 0
while mint <= maxt:
    mid = (mint + maxt) // 2
    balloon_count = balloon(mid)
    if balloon_count < m:
        mint = mid + 1
    else:
        maxt = mid - 1

print(mint)

