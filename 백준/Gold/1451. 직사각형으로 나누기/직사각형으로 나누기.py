n, m = map(int, input().split())
square = list(list(int(i) for i in input()) for _ in range(n))
answer = 0
# 1.
for i in range(1, n):
    for j in range(1, m):
        a = sum(sum(item) for item in [square[k][:j] for k in range(i)])
        b = sum(sum(item) for item in [square[k][j:] for k in range(i)])
        c = sum(sum(item) for item in [square[k][:j] for k in range(i, n)])
        d = sum(sum(item) for item in [square[k][j:] for k in range(i, n)])
        answer = max(answer, max(a*b*(c+d), a*c*(b+d), (a+b)*c*d, (a+c)*b*d))

# 2. 세로 3등분
for j in range(m):
    for jj in range(j, m):
        a = sum(sum(item) for item in [square[k][:j] for k in range(n)])
        b = sum(sum(item) for item in [square[k][j:jj] for k in range(n)])
        c = sum(sum(item) for item in [square[k][jj:] for k in range(n)])
        answer = max(answer, a*b*c)

# 3. 가로 3등분
for i in range(n):
    for ii in range(i+1, n):
        a = sum(sum(item) for item in [square[k][:] for k in range(i)])
        b = sum(sum(item) for item in [square[k][:] for k in range(i, ii)])
        c = sum(sum(item) for item in [square[k][:] for k in range(ii, n)])
        answer = max(answer, a*b*c)

print(answer)