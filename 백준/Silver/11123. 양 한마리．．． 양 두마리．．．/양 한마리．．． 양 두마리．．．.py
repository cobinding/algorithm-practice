import sys;input=sys.stdin.readline
sys.setrecursionlimit(2000)
from collections import deque 

d = [(1,0), (-1,0), (0,1), (0,-1)]
t = int(input())

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if (0 <= nx < h) and (0 <= ny < w):
                if(not visited[nx][ny]) and (graph[nx][ny] == '#'):
                    q.append((nx, ny))
                    visited[nx][ny] = True

            
for _ in range(t):
    h, w = map(int, input().split())
    graph = [input().rstrip() for _ in range(h)]
    visited = [[False]*(w) for _ in range(h)]
    answer = 0
    
    for i in range(h):
        for j in range(w):
            if (not visited[i][j]) and (graph[i][j] == '#'): 
                bfs(i, j)
                answer += 1

    print(answer)