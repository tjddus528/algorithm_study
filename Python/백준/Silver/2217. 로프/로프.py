n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

max_weight = 0
for num, l in enumerate(rope):
    if max_weight < (num+1) * l:
        max_weight = (num+1) * l

print(max_weight)

