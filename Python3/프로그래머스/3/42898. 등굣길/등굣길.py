def solution(m, n, puddles):
    answer = 0
    INF = int(1e9)
    maps = [[0]*(m+1) for _ in range(n+1)]
    
    maps[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                continue
            if i == 1 and j == 1:
                continue
            maps[i][j] = maps[i][j-1] + maps[i-1][j]
            
            # for a in range(1, n+1):
            #     for b in range(1, m+1):
            #         print(maps[a][b], end = ' ')
            #     print()
            # print()
    answer = maps[n][m]
    return answer%1000000007