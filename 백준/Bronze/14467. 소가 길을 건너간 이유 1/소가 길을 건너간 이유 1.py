import sys; input=sys.stdin.readline

n = int(input())
d = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[]}
for _ in range(n):
    key, where = map(int, input().split())
    d[key].append(where)

cnt = 0
for item in d.items():
    if len(item[1]) > 1:
        for i in range(1, len(item[1])):
            if item[1][i-1] != item[1][i]:
                cnt += 1

print(cnt)