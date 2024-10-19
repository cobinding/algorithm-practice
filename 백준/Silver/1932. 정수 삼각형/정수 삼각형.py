import sys; input=sys.stdin.readline

n = int(input())

triangle = []
for i in range(n):
    tmp = list(map(int, input().split()))
    triangle.append(tmp)

for i in range(n):
    triangle[i] = triangle[i] + [0] * (n - i -1)

dp = [[0]*(n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] = max(triangle[i][j]+dp[i-1][j],
                    triangle[i][j]+dp[i-1][j-1])

find_max = []
for item in dp:
    find_max.append(max(item))

print(max(find_max))