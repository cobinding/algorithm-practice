import sys; input = sys.stdin.readline
sys.setrecursionlimit(20000)

d = [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]

def dfs(x,y):
    visited[x][y] = True
    
    for dx, dy in d:
        nx, ny = x+dx, y+dy 
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny) 
    
# H: 행, W: 열
while True:
    w, h = map(int, input().split())
    visited = [[False]*w for _ in range(h)]
    graph = [list(map(int, input().rsplit())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j] : 
                dfs(i, j)
                cnt += 1

    if w == 0 and h == 0:
        break
    else:
        print(cnt)