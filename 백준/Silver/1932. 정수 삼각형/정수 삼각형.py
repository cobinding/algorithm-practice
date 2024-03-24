n=int(input())
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

graph[1][1] = int(input())
dp[1][1] = graph[1][1]


for i in range(2, n+1):
    tmp = list(map(int,input().split()))
    for j in range(1, n+1):
        for k in range(len(tmp)):
            graph[i][k+1] = tmp[k]
                
                
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j]+graph[i][j], dp[i-1][j-1]+graph[i][j])

ans = 0
for item in dp:
    ans = max(ans, max(item))

print(ans)