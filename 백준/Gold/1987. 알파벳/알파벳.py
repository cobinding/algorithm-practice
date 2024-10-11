from sys import stdin, setrecursionlimit
setrecursionlimit(3000)
input=stdin.readline

r,c = map(int, input().split())
graph = [input().rstrip() for _ in range(r)]
alphabet = [False] * (ord('Z')-ord('A')+1)
dr = [(1,0),(-1,0),(0,1),(0,-1)]
max_cnt = 0

def dfs(y,x,cnt):
    global max_cnt
    alphabet[ord(graph[y][x])-65] = True

    max_cnt = max(max_cnt, cnt)
    for dx, dy in dr:
        nx, ny = x+dx, y+dy

        if 0 <= ny < r and 0 <= nx < c :
            alpha = graph[ny][nx]
            if not alphabet[ord(alpha)-65]:
                alphabet[ord(alpha)-65] = True
                dfs(ny,nx,cnt+1)
                alphabet[ord(alpha) - 65] = False

dfs(0,0,1)
print(max_cnt)