import sys;input=sys.stdin.readline
from collections import deque

def bfs(y,x):
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(y,x,cnt)])
    visited[y][x] = True

    while q :
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        cnt = tmp[2]

        for dy, dx in d:
            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if graph[ny][nx] == "L":
                    q.append((ny, nx, cnt+1))
                    visited[ny][nx] = True
    return cnt


n,m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
d = [(0,1),(0,-1),(1,0),(-1,0)]

res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            count = bfs(i,j)
            res.append(count)
print(max(res))