import sys;input=sys.stdin.readline

n=int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0] * (n)

if n <= 2 :
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = max(stairs[0] + stairs[1], stairs[1])
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        case1 = dp[i-3] + stairs[i-1] + stairs[i]
        case2 = dp[i-2] + stairs[i]
        dp[i] = max(case1, case2)

    print(dp[-1])