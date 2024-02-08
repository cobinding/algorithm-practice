import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)

# m: 행 n: 열
m,n = map(int, input().split())
graph = [input().rstrip() for _ in range(m)]
visited = [[False]*n for _ in range(m)]
d = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(x,y):
    visited[x][y] = True
    
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == '0':
                visited[nx][ny] = True 
                dfs(nx, ny)    
                if nx == m-1: print("YES"); exit()
                

for j in range(n):
        if graph[0][j] == '0' and not visited[0][j]:
            dfs(0,j)

print("NO")