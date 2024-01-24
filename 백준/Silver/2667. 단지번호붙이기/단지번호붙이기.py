import sys;input=sys.stdin.readline
sys.setrecursionlimit

n = int(input())
graph = [input().rstrip() for _ in range(n)]
visited = [[False]*(n) for _ in range(n)]
d = [(0,1),(1,0),(-1,0),(0,-1)]

num_house = []
cnt = 1

def dfs(x, y, cnt):
    visited[x][y] = True
    
    for dx, dy in d :
        nx, ny = x+dx, y+dy
        if (0 <= nx < n) and (0 <= ny < n) and (not visited[nx][ny]):
            if graph[nx][ny] == '1':
                cnt = dfs(nx, ny, cnt+1)
                visited[nx][ny] = True
    return cnt 
    
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
    
            num_house.append(dfs(i, j, cnt))

print(len(num_house))
for item in sorted(num_house):
    print(item)