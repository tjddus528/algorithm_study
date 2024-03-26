n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [0] * (k+1)
coins.sort()

d[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        d[i] += d[i-coin]

print(d[k])