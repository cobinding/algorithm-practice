import sys; input=sys.stdin.readline
from collections import deque

# n: 열, m: 행
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
d = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
cnt = 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = True

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 :
            # 익은 토마토 위치를 미리 Queue에 삽입
            q.append((i,j))

bfs()
   
ans = 0     
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 :
            print(-1)
            exit()
    ans = max(ans, max(graph[i]))

print(ans-1)