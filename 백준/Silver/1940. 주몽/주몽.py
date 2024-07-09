import sys;input=sys.stdin.readline

n=int(input())
m=int(input())
arr=sorted(map(int,input().split()))

start,end=0,n-1
ans=0

while start<end and start>=0 and end<n:
   
    numbers=arr[start]+arr[end]
    
    if numbers<m: start+=1
    elif numbers>m: end-=1
    else: ans+=1; start+=1

print(ans)