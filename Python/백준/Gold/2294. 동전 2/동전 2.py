n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

INF = int(1e9)
d = [INF] * (k+1)
for coin in coins:
    if coin <= k:
        d[coin] = 1

for i in range(coins[0]+1, k+1):
    for coin in coins:
        if i > coin:
            d[i] = min(d[i-coin]+1, d[i])

result = d[k]
if result >= INF:
    print(-1)
else:
    print(result)
