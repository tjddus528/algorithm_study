data = list(map(int, input().split()))
rate = [[] for _ in range(8)]

start, end = 0, 6
for i in range(8):
    for j in range(0, i+1):
        rate[i].append(0)
    for j in range(start, end+1):
        rate[i].append(round(data[j]*0.01, 10))
    for j in range(0, i+1):
        rate[i][j] = 1 - rate[j][i] if i != j else 0
    gap = end - start
    start = end + 1
    end = start + gap - 1

def round1(i):
    return rate[i][i-1 if i%2 else i+1]
def round2(i):
    if i in (0, 1): a = (2, 3)
    elif i in (2, 3): a = (0, 1)
    elif i in (4, 5): a = (6, 7)
    elif i in (6, 7): a = (4, 5)
    return round1(i) * sum(round1(aa) * rate[i][aa] for aa in a)
def final(i):
    if i in (0, 1, 2, 3): a = (4, 5, 6, 7)
    elif i in (4, 5, 6, 7): a = (0, 1, 2, 3)
    return round2(i) * sum(round2(aa) * rate[i][aa] for aa in a)

for i in range(8):
    print(round(final(i), 9), end = ' ')