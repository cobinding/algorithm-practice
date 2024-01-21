import sys;input=sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())
m = int(input())

visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
cnt = 0

for _ in range(m):
    x, y = map(int, input().rsplit())
    graph[x].append(y)
    graph[y].append(x)

# 인접 노드 방문
def dfs(x, cnt):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    return cnt

print(dfs(1, 0))