n = int(input())
m = int(input())
data = [0] + list(int(item) for item in input().split(' '))

max_gap = 0
for i in range(m+1):
    if i == 0: gap = data[1]
    elif i == m: gap = n - data[i]
    else: gap = (data[i+1] - data[i] + 1) // 2
    max_gap = max(gap, max_gap)
print(max_gap)