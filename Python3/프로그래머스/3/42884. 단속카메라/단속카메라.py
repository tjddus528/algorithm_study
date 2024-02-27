def solution(routes):
    answer = 0
    camera = []
    checked = [False] * len(routes)
    # 1. 시작지점 기준으로 정렬
    routes.sort(key = lambda x : x[0])
    camera.append(routes[0])
    checked[0] = True
    for i in range(1, len(routes)):
        start = routes[i][0]
        end = routes[i][1]
        for c in camera:
            if c[0] <= end and c[1] >= start:
                c[0] = max(c[0], start)
                c[1] = min(c[1], end)
                checked[i] = True
                break
        if not checked[i]:
            camera.append(routes[i])
        # print(camera)
        
    return len(camera)