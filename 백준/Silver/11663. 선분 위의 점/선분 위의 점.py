import sys;input=sys.stdin.readline

n,m=map(int,input().split())
points=sorted(map(int,input().split()))

def lower_bound(target):
    low_idx=n
    start,end=0,n-1

    while start<=end:
        mid=(start+end)//2
        if points[mid] >= target:
            low_idx=min(low_idx,mid)
            end=mid-1
        else:
            start=mid+1
    return low_idx

def upper_bound(target):
    up_idx=n
    start,end=0,n-1

    while start<=end:
        mid=(start+end)//2
        if points[mid] > target:
            up_idx=min(up_idx,mid)
            end=mid-1
        else:
            start=mid+1
    return up_idx

for _ in range(m):
    x1,x2=map(int,input().split())
    cnt=upper_bound(x2)-lower_bound(x1)
    print(cnt)