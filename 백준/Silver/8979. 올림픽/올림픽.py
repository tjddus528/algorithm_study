n, k = map(int, input().split())
countries = {}
for _ in range(n):
    number, gold, silver, bronze = map(int, input().split())
    countries[number] = [gold, silver, bronze]

target = countries[k]
rank = 1
for country in countries:
    if country == k: continue
    g, s, b = countries[country]
    if g > target[0]: rank += 1
    elif g == target[0]:
        if s > target[1]: rank += 1
        elif s == target[1]:
            if b > target[2]: rank += 1

print(rank)