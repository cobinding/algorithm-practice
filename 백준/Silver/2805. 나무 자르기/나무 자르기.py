import sys;input=sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))
left,right=1,max(tree)
ans=0
while left<=right:
    mid=(left+right)//2
    
    total=0
    for item in tree:
        if item > mid :
            total += (item-mid)

    if total<m:
        right=mid-1
    else: 
        left=mid+1
        ans=mid
        
print(ans)