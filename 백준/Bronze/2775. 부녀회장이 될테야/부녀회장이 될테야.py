import sys;input=sys.stdin.readline

t=int(input())


# k층 n호에 몇명이 살고있을까?
for _ in range(t):
    k=int(input())
    n=int(input())

    if k <= 1:
        dp = [0] * 15
        for i in range(1, 15): # 1호 ~ 14호
            dp[i] = dp[i-1] + i
        print(dp[n])

    else:
        dp = [[0]*15 for _ in range(15)]

        # 2층 채우기
        for i in range(1,15):
            dp[1][i] = dp[1][i-1] + i

        for i in range(2, 15): # 2층 ~ 14층
            for j in range(1, 15): # 1호 ~ 14호
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        print(dp[k][n])