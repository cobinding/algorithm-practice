import sys;input=sys.stdin.readline

n=int(input())
card=list(map(int, input().split()))
m=int(input())
check=list(map(int, input().split()))

d=dict()

for item in card:
    if d.get(item):
        d[item] += 1
    else:
        d[item] = 1
    

for item in check:
    if d.get(item):
        print(d[item], end=' ')
    else:
        print(0, end=' ')