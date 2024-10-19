import sys; input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    
    dp=[0 for _ in range(12)]
    dp[0],dp[1],dp[2],dp[3] = 0,1,2,4
    
    for i in range(4, n+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
        
    print(dp[n])