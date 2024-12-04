n = int(input())
data = list(input() for _ in range(n))
friends = [set() for _ in range(n)]
cnt_list = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if data[i][j] == 'Y':
            friends[i].add(j)
            continue
        for k in range(n):
            if data[i][k] == 'Y' and data[k][j] == 'Y':
                friends[i].add(j)
    cnt_list[i] = len(friends[i])
print(max(cnt_list))
