import sys;input=sys.stdin.readline

n=int(input())
tree=list(map(int,input().split()))
k=int(input())

visited=[False for _ in range(n)]
graph=[[] for _ in range(n)]

# index: 부모, 값: 자식
for i in range(n):
    # root인 경우
    if tree[i] == -1 : 
        continue
    else:
        graph[tree[i]].append(i)

def dfs(x):
    visited[x] = True
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            graph[i].append(100)
    graph[x].append(100)

dfs(k)
cnt=0
for i in graph:
    if k in i and len(i) == 1 :
        cnt += 1
    if len(i) == 0 :
        cnt += 1

print(cnt)