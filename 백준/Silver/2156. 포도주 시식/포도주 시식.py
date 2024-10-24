import sys;input=sys.stdin.readline

n=int(input())
arr=[int(input()) for _ in range(n)]
dp=[0 for _ in range(n)]

dp[0] = arr[0]

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
elif n == 3:
    print(max(arr[0]+arr[1], arr[1]+arr[2], arr[0]+arr[2]))

else:
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])

    for i in range(2, n):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2], dp[i-1])

    print(max(dp))