import sys; input=sys.stdin.readline

graph = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    a, b, c, d = map(int, input().rsplit())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1

cnt = 0
for item in graph:
    cnt += sum(item)
print(cnt)