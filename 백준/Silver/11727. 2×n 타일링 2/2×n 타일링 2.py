n=int(input())

dp=[0 for _ in range(n+1)]
dp[0], dp[1] = 1, 1

for i in range(1, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

if n == 1 : 
    print(1)
else: 
    print(dp[-1]%10007)