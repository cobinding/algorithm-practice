import sys; input=sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

total = 0
for i in range(n):
    total += sum(arr[:i+1])

print(total)