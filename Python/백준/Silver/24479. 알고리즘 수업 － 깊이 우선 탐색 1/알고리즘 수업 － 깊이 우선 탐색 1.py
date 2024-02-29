import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = []
for _ in range(n+1):
    graph.append([])
for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(graph[a], b)
    heapq.heappush(graph[b], a)



visited = [False] * (n+1)
result = [0] * (n+1)
def dfs(start):
    cnt = 1
    stack = [start]
    result[start] = cnt
    visited[start] = True
    while stack:
        now = stack.pop()

        while graph[now]:
            next = heapq.heappop(graph[now])
            if not visited[next]:
                visited[next] = True
                stack.append(now)
                stack.append(next)
                cnt += 1
                result[next] = cnt
                break


dfs(r)
for i in range(1, n+1):
    print(result[i])