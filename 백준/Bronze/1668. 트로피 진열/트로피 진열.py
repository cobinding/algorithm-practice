import sys;input=sys.stdin.readline

n=int(input().rstrip())
trophy=[int(input().rstrip()) for _ in range(n)]

l_max_val=0
l_cnt=0
for i in range(n):
    if trophy[i] > l_max_val:
        l_max_val=trophy[i]
        l_cnt+=1     

r_max_val=0
r_cnt=0
for i in range(n-1,-1,-1):
    if trophy[i] > r_max_val:
        r_max_val=trophy[i]
        r_cnt+=1

print(l_cnt)
print(r_cnt) 