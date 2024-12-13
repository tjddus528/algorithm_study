n, k = map(int, input().split())
data = list(input())

cnt = 0
for i in range(n):
    if data[i] == 'P':
        for h in range(i-k, i+k+1):
            if 0 <= h <= n-1 and data[h] == 'H':
                data[h] = 'X'
                cnt += 1
                break
print(cnt)
