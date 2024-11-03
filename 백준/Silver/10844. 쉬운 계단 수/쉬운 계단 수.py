import sys;input=sys.stdin.readline

n = int(input())

# (자릿수, 끝값 ) - 끝값마다 자릿수가 추가될 때의 규칙성이 다름
dp = [[0]* 10 for _ in range(n+1)]

# 한 자릿수 값 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):

        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif 0 < j < 9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)