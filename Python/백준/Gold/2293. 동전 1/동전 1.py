n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [0] * (k+1)
coins.sort()

for i in range(coins[0], k+1, coins[0]):
    d[i] = 1

for cidx in range(1, n):
    for i in range(coins[cidx]+1, k+1):
        d[i] = d[i] + d[i-coins[cidx]]
    for i in range(coins[cidx], k+1, coins[cidx]):
        d[i] = d[i] + 1

print(d[k])