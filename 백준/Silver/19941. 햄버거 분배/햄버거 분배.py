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



# 순차적으로 사람을 만날 때마다 햄버거를 먹을 수 있으면 먹이기
# 가장 앞쪽 햄버거부터 먹을 수 있는 햄버거 먹기
# 먹은 햄버거 자리에 표시

# ex)
# 12 1
# HPHPHPHHPPHP
# 12 2
# HPHPHPHHPPHP
# 12 5
# PPHHHPHPHHPP
# 6 2
# PHHHPP
