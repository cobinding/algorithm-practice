import sys; input=sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque([(i,j)])
    is_peak = True
    visited[i][j] = True

    while q :
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for dy, dx in d :
            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < m:
                # 산봉우리가 될 수 있으면 탐색
                if graph[y][x] == graph[ny][nx] and not visited[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                # 주변이 하나라도 크면 탐색 X
                elif graph[y][x] < graph[ny][nx]:
                    is_peak = False

    return is_peak

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
d = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

cnt = 0
for i in range(n): # y
    for j in range(m): # x
        if not visited[i][j]:
            if bfs(i,j):
                cnt += 1

print(cnt)