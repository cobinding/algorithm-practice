import sys;input=sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [(-1,0),(1,0),(0,1),(0,-1)]
q = deque()

def bfs(y,x,rain):
    q.append((y,x))

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if graph[ny][nx] > rain:
                    q.append((ny,nx))
                    visited[ny][nx] = True


result = []
for rain in range(1, 101):
    tmp = 0
    visited = [[False] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                # 해당 지점 > 주변 탐색 > 주변이 모두 잠기면(if graph[ny][nx] > rain : q.append) return
                # 즉, 경계마다 return
                bfs(i,j,rain)
                visited[i][j] = True
                tmp += 1
    result.append(tmp)

res = max(result)
print(1) if res == 0 else print(res)