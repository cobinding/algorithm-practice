n,m=map(int,input().split())

scope=[list(map(int,input().split())) for _ in range(n)]
dp=[[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = scope[0][0]

# 가장 윗줄 채워주기
for i in range(m):
    dp[0][i] = dp[0][i-1] + scope[0][i]
    
# 가장 왼쪽줄 채워주기
for i in range(n):
    dp[i][0] = dp[i-1][0] + scope[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i][j-1]+scope[i][j], dp[i-1][j]+scope[i][j])

ans=0
for item in dp:
    ans = max(ans, max(item))

if n == 1 and m == 1 and scope[0][0] == 1:
    print(1)
else:
    print(ans)