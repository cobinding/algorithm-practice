import sys; input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
k = 0
b = [0]*(n)
start = min(a)
end = max(a)

for i in range(start, end+1):
    for j in range(n):
        if a[j] == i :
            b[j] = k
            k += 1
print(*b)           