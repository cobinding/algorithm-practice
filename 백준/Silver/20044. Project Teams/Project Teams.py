import sys; input = sys.stdin.readline

n = int(input().rstrip())
students = sorted(map(int, input().rstrip().split()))

temp = []
for i in range(n):
    temp.append(students[i] +students[n*2-i-1])
    
print(min(temp))