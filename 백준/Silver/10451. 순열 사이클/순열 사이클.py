import sys; input = sys.stdin.readline
sys.setrecursionlimit(2000)

t = int(input())

# 주변 노드 탐색
def dfs(x) :
    visited[x] = True
    next = li[x]
    
    if not visited[next]:
        dfs(next)
    
for _ in range(t):
    n = int(input().rstrip())
    li = [0] + list(map(int, input().rsplit()))

    visited = [False] * (n+1)
    answer = 0 
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    print(answer)