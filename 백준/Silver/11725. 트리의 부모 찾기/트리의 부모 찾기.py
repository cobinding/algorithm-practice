import sys; input = sys.stdin.readline
sys.setrecursionlimit(200000)

n = int(input().rstrip())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            ans[i] = x
            
for _ in range(n-1):
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)

for i in range(1, n+1):
    dfs(i)

for i in range(2, n+1):
    print(ans[i])