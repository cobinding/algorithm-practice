import sys; input=sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    file = input().rstrip()
    
    for i in range(len(file)):
        if file[i] == '.':
            key = file[i+1:]
            break
    
    if d.get(key):
        d[key] += 1
    else:
        d[key] = 1

ans = sorted(d.items(), key = lambda x:x[0])
for k, v in ans:
    print(k, v)