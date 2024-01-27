import sys;input=sys.stdin.readline
sys.setrecursionlimit(20000)

m,n,k = map(int, input().split())
direction = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[False]*(n) for _ in range(m)]
graph = [[0]*(n) for _ in range(m)]

def dfs(y, x, cnt):
    visited[y][x] = True
    
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        
        if (0 <= nx < n) and (0 <= ny < m):
            if (graph[ny][nx] == 0) and (not visited[ny][nx]):
                visited[ny][nx] = True
                cnt = dfs(ny, nx, cnt+1)
                
    return cnt      
            
# 좌표를 통해 사각형 정의하기 
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1
            
ans, cnt = 0, 1
area = []
for j in range(m):
    for i in range(n):
        if (graph[j][i] == 0) and (not visited[j][i]):
            tmp = dfs(j, i, cnt)
            area.append(tmp)
            ans += 1


print(ans)
print(*sorted(area))