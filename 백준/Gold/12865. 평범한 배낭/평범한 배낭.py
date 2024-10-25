import sys;input=sys.stdin.readline

n,k = map(int, input().split())

items = [(0,0)]
for _ in range(n):
    w,v = map(int, input().split())
    items.append((w,v))

dp = [[0]*(k+1) for _ in range(n+1)]

# 행: 물건 수(n), 열: 최대 무게(k)

for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i][0] # 무게
        v = items[i][1] # 가치

        # 현재 용량보다 물건의 무게가 클 경우 -> 넣지 않는다. 즉, 이전 값과 같다.
        if j < w :
            dp[i][j] = dp[i-1][j]
        # (현재 용량 - 물건 무게)에서 가치를 더한 값이 더 큰지 확인한다.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])