n = int(input())
data = list(map(int, input().split()))

def bs(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < target: left = mid + 1
        else: right = mid
    return right

lst = [0 for _ in range(n+1)]
i, j = 1, 0
lst[0] = data[0]
while i < n:
    if lst[j] < data[i]:
        lst[j+1] = data[i]
        j += 1
    else:
        idx = bs(0, j, data[i])
        lst[idx] = data[i]
    i += 1
print(j+1)
