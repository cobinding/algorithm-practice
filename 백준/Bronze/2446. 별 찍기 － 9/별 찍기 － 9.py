import sys; input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    print(' ' * (i-1) + ('*' * (n*2 - (2*i - 1))))

for i in range(2, n+1):
    print(' ' * (n-i) + ('*' * (2*i - 1)))