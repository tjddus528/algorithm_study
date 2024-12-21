n = int(input())
left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    if mid**2 > n: right = mid - 1
    elif mid**2 < n: left = mid + 1
    else:
        print(mid)
        break