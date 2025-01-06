import sys;input=sys.stdin.readline

n = 1000000
d = [1] * (n+1)

"""for i in range(2, n+1):
    for j in range(1, n+1):
        if i*j <= n:
            d[i*j] += i"""

for i in range(2, n+1):
    j = 1
    while i*j <= n:
        d[i*j] += i
        j += 1

# g(n): 1~n 약수들의 합
g = [0] * (n+1)
for i in range(1, n+1):
    g[i] = g[i-1] + d[i]

t = int(input())
for _ in range(t):
    num = int(input())
    print(g[num])